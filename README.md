
 # Video Search & Upload Platform



This platform offers users the capability to upload videos and then search through them using keywords found in the subtitles.

## Features
- Video Upload: Users can easily upload their videos.
- Subtitles Extraction: Once a video is uploaded, the system extracts subtitles for search functionalities.
- Keyword Search: Allows users to search for videos using specific keywords or phrases from the subtitles.


## Getting Started
### Prerequisites
- Python 3.11.3
- Django 4.2.4
### for linux version https://github.com/lathifshaik/Serch_video_with_subtitles/tree/fixed
### Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/lathifshaik/Serch_video_with_subtitles.git

2. Navigate to the project directory:
   ```sh
   cd video-platform

3. Activate the virtual environment:
   ```sh
   #source venv/bin/activate
4. Install required packages:
    ```sh
    pip install -r requirements.txt
    
5. Migrate the database:
   ```sh
   python manage.py migrate
6. Run the development server:
   ```sh
   python manage.py runserver
   
The platform should be running at http://127.0.0.1:8000/.

### Usage:
-Uploading Videos: Navigate to the upload page and select your video file to upload.
-Searching Videos: On the search page, enter a keyword or phrase. The platform will display videos where the subtitles match the search query.
### Contributing
Contributions are welcome! Follow these steps:

Fork the project.
Create your feature branch: git checkout -b feature/YourFeature
Commit your changes: git commit -m 'Add YourFeature'
Push to the branch: git push origin feature/YourFeature
Open a pull request.


Contact
Your Name - i.lathifshaik@gmail.com

Project Link: https://github.com/lathifshaik/Serch_video_with_subtitles



