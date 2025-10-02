from sample_app.adapters import LocalCSVSource, InMemorySink
from sample_app.pipeline import SumByCategory, run_pipeline
from pathlib import Path

def test_sum_by_category(tmp_path: Path):
    # arrange
    input_csv = tmp_path / "in.csv"
    input_csv.write_text("category,value\nA,1\nA,2\nB,3\n", encoding="utf-8")

    sink = InMemorySink()

    # act
    run_pipeline(LocalCSVSource(str(input_csv)), SumByCategory(), sink)

    # assert
    # order doesn't matter; convert to dict
    got = {row["category"]: float(row["total_value"]) for row in sink.data}
    assert got["A"] == 3.0
    assert got["B"] == 3.0
