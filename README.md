# mkpipe-loader-redshift

Amazon Redshift loader plugin for [MkPipe](https://github.com/mkpipe-etl/mkpipe). Writes Spark DataFrames into Redshift tables via JDBC.

## Documentation

For more detailed documentation, please visit the [GitHub repository](https://github.com/mkpipe-etl/mkpipe).

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

---

## Connection Configuration

```yaml
connections:
  redshift_target:
    variant: redshift
    host: my-cluster.abc123.us-east-1.redshift.amazonaws.com
    port: 5439
    database: mydb
    schema: public
    user: myuser
    password: mypassword
```

---

## Table Configuration

```yaml
pipelines:
  - name: pg_to_redshift
    source: pg_source
    destination: redshift_target
    tables:
      - name: public.events
        target_name: public.stg_events
        replication_method: full
        batchsize: 10000
```

---

## Write Parallelism & Throughput

```yaml
      - name: public.events
        target_name: public.stg_events
        replication_method: full
        batchsize: 10000
        write_partitions: 4
```

- **`batchsize`**: rows per JDBC batch insert.
- **`write_partitions`**: reduces concurrent JDBC connections via `coalesce(N)`.

### Performance Notes

- For large loads, Redshift's native `COPY` from S3 is significantly faster than JDBC. JDBC is suitable for moderate-sized writes.
- Redshift performs better with fewer, larger transactions — increase `batchsize` and reduce `write_partitions` for big loads.

---

## All Table Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `name` | string | required | Source table name |
| `target_name` | string | required | Redshift destination table name |
| `replication_method` | `full` / `incremental` | `full` | Replication strategy |
| `batchsize` | int | `10000` | Rows per JDBC batch insert |
| `write_partitions` | int | — | Coalesce DataFrame to N partitions before writing |
| `dedup_columns` | list | — | Columns used for `mkpipe_id` hash deduplication |
| `tags` | list | `[]` | Tags for selective pipeline execution |
| `pass_on_error` | bool | `false` | Skip table on error instead of failing |
