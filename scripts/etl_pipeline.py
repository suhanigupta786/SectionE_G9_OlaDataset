"""
ETL pipeline for OLA Ride Analysis Project
"""

from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd
import numpy as np


# ─── Normalize Columns ─────────────────────────────────────
def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    return df


# ─── Cleaning ──────────────────────────────────────────────
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = normalize_columns(df)

    # Replace missing values
    df = df.replace(["unknown", "NA", "-", ""], np.nan)

    # Fill missing values
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna("unknown").str.lower().str.strip()
        else:
            df[col] = df[col].fillna(df[col].median())

    # Convert types
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["hour"] = pd.to_numeric(df["hour"], errors="coerce")

    # Remove duplicates
    df = df.drop_duplicates().reset_index(drop=True)

    return df


# ─── Feature Engineering ───────────────────────────────────
def add_features(df: pd.DataFrame) -> pd.DataFrame:

    # Success flag
    df["is_successful"] = df["booking_status"] == "success"

    # Cancellation flag
    df["cancel_flag"] = df["booking_status"].str.contains("cancel", na=False)

    # Time of Day
    def get_time_of_day(h):
        if pd.isna(h):
            return "unknown"
        if h < 6:
            return "early_morning"
        elif h < 12:
            return "morning"
        elif h < 18:
            return "afternoon"
        elif h < 22:
            return "evening"
        else:
            return "late_night"

    df["time_of_day"] = df["hour"].apply(get_time_of_day)

    # Revenue Lost (for cancelled rides)
    avg_revenue = df["revenue"].mean()
    df["revenue_lost"] = np.where(
        df["is_successful"], 0, avg_revenue
    )

    return df


# ─── Build Dataset ─────────────────────────────────────────
def build_dataset(input_path: Path) -> pd.DataFrame:
    df = pd.read_csv(input_path)
    df = clean_data(df)
    df = add_features(df)
    return df


# ─── Save Output ───────────────────────────────────────────
def save_processed(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


# ─── CLI ──────────────────────────────────────────────────
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run OLA ETL pipeline")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args()


# ─── Main ─────────────────────────────────────────────────
def main() -> None:
    args = parse_args()
    df = build_dataset(args.input)
    save_processed(df, args.output)

    print(f"Processed dataset saved to: {args.output}")
    print(f"Rows: {len(df)} | Columns: {len(df.columns)}")


if __name__ == "__main__":
    main()
