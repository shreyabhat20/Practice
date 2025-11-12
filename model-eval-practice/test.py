import os
import pandas as pd
import mlflow
from openai import OpenAI
os.environ["TIKTOKEN_VERIFY_SSL"] = "0"
client = OpenAI()

eval_data = pd.DataFrame(
    {
        "inputs": [
            "What is MLflow?",
            "What is Apache Spark?",
        ],
        "ground_truth": [
            "MLflow is an open-source platform for managing the machine learning lifecycle, including experiment tracking, model registry, and deployment.",
            "Apache Spark is an open-source distributed computing framework designed for large-scale data processing and analytics.",
        ],
    }
)

mlflow.set_tracking_uri("sqlite:///mlflow.db")  
mlflow.set_experiment("LLM Evaluation")

with mlflow.start_run():
    system_prompt = "Answer the following question in two sentences."

    logged_model_info = mlflow.openai.log_model(
        model="gpt-4o-mini",
        task="chat.completions", 
        artifact_path="model",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "{inputs}"},
        ],
    )

    results = mlflow.evaluate(
        logged_model_info.model_uri,
        eval_data,
        targets="ground_truth",
        model_type="question-answering",
        extra_metrics=[
            mlflow.metrics.genai.answer_similarity(),
            mlflow.metrics.latency(),
            mlflow.metrics.toxicity(),
        ],
    )

    print("Aggregated Metrics:\n", results.metrics)

    eval_table = results.tables["eval_results_table"]
    df = pd.DataFrame(eval_table)
    df.to_csv("eval_results.csv", index=False)
    print("Saved evaluation results to eval_results.csv")
