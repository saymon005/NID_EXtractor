import requests
from django.shortcuts import render
from .forms import ImageUploadForm

def upload_image(request):
    result = None
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # FastAPI endpoint URL
            api_url = "https://fastapi2-476477490775.us-central1.run.app/generate"  # Your FastAPI URL

            # Get the uploaded file
            uploaded_file = request.FILES['image']

            # Set MIME type (e.g., 'image/jpeg', 'image/png')
            mime_type = uploaded_file.content_type

            # Prepare the file and headers for the request
            files = {'image': (uploaded_file.name, uploaded_file, mime_type)}

            try:
                # Send the request to FastAPI
                response = requests.post(api_url, files=files, timeout=30)

                if response.status_code == 200:
                    # Get the response JSON
                    result = response.json()
                    #print(result)  # This will print the JSON response

                    # Process the data as per your format by removing apostrophes and spaces from keys
                    processed_result = {
                        "message": result.get('message', 'No message'),
                        "document_id": result.get('document_id'),
                        "data": {
                            "Name": result['data'].get("Name"),
                            "Fathers_Name": result['data'].get("Father's Name"),
                            "Mothers_Name": result['data'].get("Mother's Name"),
                            "Date_of_Birth": result['data'].get("Date of Birth"),
                            "ID_No": result['data'].get("ID No"),
                            "Address": result['data'].get("Address"),
                            "Blood_Group": result['data'].get("Blood Group"),
                        }
                    }
                    
                    # Update the result to pass to the template
                    result = processed_result
                    #print(result)  # This prints the processed result
                    
                else:
                    result = {"error": f"API returned a status code {response.status_code}"}
            
            except Exception as e:
                #result = {"error": f"An error occurred: {str(e)}"}
                result = {"error": "This is not a valid NID!"}

    else:
        form = ImageUploadForm()

    # Render the form and pass the API result to the template
    return render(request, 'upload_image.html', {'form': form, 'result': result})
