import requests
import gradio as gr

# Function to get Access Token
def get_access_token():
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": "joBfSRbSoL1deQkdETpcrUe-GLg5k6bg63_U9Xwb82NV"
    }
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise Exception("Error obtaining access token: " + response.text)

access_token = get_access_token()

# Define API endpoint and headers
url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

def get_summary(transcript):
    # Define the request body
    body = {
        "input": f"""Write a short summary for the following meeting transcript.

Transcript: {transcript}
Summary:""",
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 800,  
            "min_new_tokens": 100,
            "repetition_penalty": 1
        },
        "model_id": "google/flan-ul2",
        "project_id": "487118e3-14e0-43b2-b88f-61fa9f4c3756",
        "moderations": {
            "hap": {
                "input": {
                    "enabled": True,
                    "threshold": 0.5,
                    "mask": {
                        "remove_entity_value": True
                    }
                },
                "output": {
                    "enabled": True,
                    "threshold": 0.5,
                    "mask": {
                        "remove_entity_value": True
                    }
                }
            }
        }
    }

    try:
        # Make the API request
        response = requests.post(url, headers=headers, json=body)

        # Check for HTTP errors
        if response.status_code != 200:
            raise Exception(f"Non-200 response: {response.text}")

        # Parse JSON response
        data = response.json()

        # Print the full API response for debugging
        print("API response:", data)

        # Extract generated text from the response
        if 'results' in data and len(data['results']) > 0:
            generated_text = data['results'][0].get('generated_text', 'No summary found')
            return generated_text
        else:
            return 'No summary found'

    except Exception as e:
        # Log and handle exceptions
        import traceback
        print("Error details:", traceback.format_exc())
        return "An error occurred while processing the transcript."

def summarize_meeting(transcript):
    summary = get_summary(transcript)
    return summary

# Gradio interface
iface = gr.Interface(
    fn=summarize_meeting,
    inputs=gr.Textbox(label="Meeting Transcript"),
    outputs=gr.Textbox(label="Summary")
)

try:
    iface.launch()
except Exception as e:
    print(f"Gradio error: {e}")
