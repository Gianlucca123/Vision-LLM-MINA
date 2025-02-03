video_length_label = document.getElementById('video-length-label')
total_frames_label = document.getElementById('total-frames-label')
video_frame_rate_label = document.getElementById('video-frame-rate-label')
frame_rate_input = document.getElementById('frame-rate-input')
total_frames_to_be_analyzed = document.getElementById('total-frames-to-be-analyzed')
start_transcription = document.getElementById('start-transcription')

var video_file_name = "";
var duration = 0;
var fps = 0;
var frame_count = 0;
var frame_rate = 0;
var total_frames = 0;

document.getElementById('load-video').onchange = function() {
    video_file_name = this.files[0].name;
    console.log("truc");

    const url = `/load-video?video_file_name=${encodeURIComponent(video_file_name)}`;

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            //console.log(data);
            duration = data.duration;
            fps = data.fps;
            frame_count = data.frame_count;
            const hours = Math.floor(data.duration / 3600);
            const minutes = Math.floor((data.duration % 3600) / 60);
            const seconds = Math.floor(data.duration % 60);
            video_length_label.innerHTML = `Video length : ${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
            video_frame_rate_label.innerHTML = "Fps : " + data.fps;
            total_frames_label.innerHTML = "Total frames : " + data.frame_count;
            compute_total_frames();
        })
        .catch(error => console.error('Error:', error));
};

// Compute total frames to be analyzed
function compute_total_frames() {
    frame_rate = frame_rate_input.value;
    total_frames = Math.floor(frame_count / (60 / (fps*frame_rate)))
    total_frames_to_be_analyzed.innerHTML = total_frames + 1 + " frames";
}

frame_rate_input.addEventListener('input', compute_total_frames);


start_transcription.onclick = function() {

    const url = `/start-transcription?video_file_name=${encodeURIComponent(video_file_name)}&frame_rate=${encodeURIComponent(frame_rate)}`;

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
        })
        .catch(error => console.error('Error:', error));
};