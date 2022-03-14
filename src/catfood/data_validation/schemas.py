import pandera as pa


no_nan_numeric_schema = pa.DataFrameSchema(
    {
        "^dma_.*": pa.Column(
            dtype=float, coerce=True, checks=pa.Check.ge(0), nullable=False, regex=True
        ),
        "^ga_.*": pa.Column(
            dtype=float, coerce=True, checks=pa.Check.ge(0), nullable=False, regex=True
        ),
    }
)
