import mlflow

mlflow.set_tracking_uri("http://localhost:5000")

run = mlflow.start_run()
print("RUN ID:", run.info.run_id)

mlflow.log_metric("test_metric", 0.5)

mlflow.end_run()