import pandas as pd

from ctr_prediction.data import load_csv, save_csv


def test_save_and_load_csv_roundtrip(tmp_path):
    df = pd.DataFrame(
        {
            "time": [1, 2, 3],
            "id": ["a", "b", "a"],
        }
    )

    out_path = tmp_path / "sample.csv"
    save_csv(df, out_path)

    loaded = load_csv(out_path)

    pd.testing.assert_frame_equal(loaded, df)
