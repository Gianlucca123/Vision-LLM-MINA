video_length_label = document.getElementById('video-length-label')
total_frames_label = document.getElementById('total-frames-label')
video_frame_rate_label = document.getElementById('video-frame-rate-label')
frame_rate_input = document.getElementById('frame-rate-input')
total_frames_to_be_analyzed = document.getElementById('total-frames-to-be-analyzed')
start_transcription = document.getElementById('start-transcription')
main_content = document.getElementById('main-content')
loading_container = document.getElementById('loading-container')
loading_bar = document.getElementById('loading-bar')
loading_percentage = document.getElementById('loading-percentage')
generated_frames = document.getElementById('generated-frames')

var video_file_name = "";
var duration = 0;
var fps = 0;
var frame_count = 0;
var frame_rate = 0;
var total_frames = 0;

document.getElementById('load-video').onchange = function() {
    video_file_name = this.files[0].name;

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

    loading_container.style.display = 'block';
    const excepted_frames = total_frames + 1
    var frame_received = 0;
    generated_frames.innerHTML = frame_received + "/" + excepted_frames + " frames";

    const url = `/start-transcription?video_file_name=${encodeURIComponent(video_file_name)}&frame_rate=${encodeURIComponent(frame_rate)}`;

    const eventSource = new EventSource(url);

    eventSource.onmessage = function(event) {
        
        //console.log("Response :", event.data);

        // replace '' by "" in event.data string
        const data = JSON.parse(event.data.replace(/'/g, "\""));
        const frame_id = data.frame_id;
        frame_received += 1;
        const answer = data.answer.replaceAll("guillemetsimple", "'").replaceAll("guillemetdouble", '"');
        const frameTime = frame_id / fps;
        const hours = Math.floor(frameTime / 3600);
        const minutes = Math.floor((frameTime % 3600) / 60);
        const seconds = Math.floor(frameTime % 60);
        const timestamp = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

        const div = document.createElement('div');
        div.className = 'bg-white p-4 rounded-lg shadow-md';

        const frameNumberP = document.createElement('p');
        frameNumberP.className = 'text-gray-700 font-semibold';
        frameNumberP.textContent = `Frame number ${frame_id}`;

        const timestampP = document.createElement('p');
        timestampP.className = 'text-gray-500 text-sm pb-5';
        timestampP.textContent = timestamp;

        const answerP = document.createElement('p');
        answerP.className = 'text-gray-600';
        answerP.innerHTML = answer;

        div.appendChild(frameNumberP);
        div.appendChild(timestampP);
        div.appendChild(answerP);

        main_content.appendChild(div);

        // Loading bar
        const percentage = Math.floor((frame_received / excepted_frames) * 100);
        loading_bar.style.width = percentage + "%";
        loading_percentage.innerHTML = percentage + "%";
        generated_frames.innerHTML = frame_received + "/" + excepted_frames + " frames";

        if (percentage == 100) {
            eventSource.close();
            loading_container.style.display = 'none';
        }
    };

    eventSource.onerror = function() {
        //console.log("Connection closed");
        eventSource.close();
    };
};


