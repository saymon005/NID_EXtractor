import requests
from django.shortcuts import render
from .forms import ImageUploadForm

def upload_image(request):
    result = None
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Replace with actual FastAPI endpoint
            api_url = "https://custom-fastapi-service-uxeku3pqoq-ue.a.run.app/generate"  # Your FastAPI URL

            # Get the uploaded file
            uploaded_file = request.FILES['image']

            # Set MIME type (e.g., 'image/jpeg', 'image/png')
            mime_type = uploaded_file.content_type

            # Prepare the file and headers for the request
            files = {'image': (uploaded_file.name, uploaded_file, mime_type)}

            try:
                # Send the request to FastAPI
                response = requests.post(api_url, files=files)

                if response.status_code == 200:
                    # Get the response JSON
                    result = response.json()
                    
                    # Process the result to replace spaces in keys with underscores
                    processed_result = {key.replace(' ', '_'): value for key, value in result['result'].items()}
                    
                    # Update the result to pass to the template
                    result = {'result': processed_result}
                    print(result)
                    
                else:
                    result = {"error": f"API returned a status code {response.status_code}"}
            
            except Exception as e:
                result = {"error": f"An error occurred: {str(e)}"}

    else:
        form = ImageUploadForm()

    # Render the form and pass the API result to the template
    return render(request, 'upload_image.html', {'form': form, 'result': result})
