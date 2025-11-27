import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def upload_file():
    with open("slm_dataset.jsonl", "rb") as f:
        file_obj = client.files.create(
            file=f,
            purpose="fine-tune"
        )
    print("Uploaded file id:", file_obj.id)
    return file_obj.id

def start_fine_tune(training_file_id: str):
    job = client.fine_tuning.jobs.create(
        training_file=training_file_id,
        model="gpt-4o-mini-2024-07-18",
        method={
            "type": "supervised",
            "supervised": {
                "hyperparameters": {
                    "n_epochs": 2
                }
            }
        },
    )
    print("Started fine-tune job id:", job.id)
    print("Status:", job.status)
    return job.id

if __name__ == "__main__":
    file_id = upload_file()
    job_id = start_fine_tune(file_id)
    print("Use this job id to check status later:", job_id)
