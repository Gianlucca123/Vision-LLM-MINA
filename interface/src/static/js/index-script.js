/**
 * @type {HTMLElement} video_length_label - Label to display the video length.
 * @type {HTMLElement} total_frames_label - Label to display the total frames of the video.
 * @type {HTMLElement} video_frame_rate_label - Label to display the frame rate of the video.
 * @type {HTMLElement} frame_rate_input - Input element for the frame rate.
 * @type {HTMLElement} total_frames_to_be_analyzed - Label to display the total frames to be analyzed.
 * @type {HTMLElement} start_transcription - Button to start the transcription process.
 * @type {HTMLElement} main_content - Main content container.
 * @type {HTMLElement} loading_container - Container for the loading bar.
 * @type {HTMLElement} loading_bar - Loading bar element.
 * @type {HTMLElement} loading_percentage - Label to display the loading percentage.
 * @type {HTMLElement} generated_frames - Label to display the number of generated frames.
 * @type {HTMLElement} prompt_input - Input element for the prompt.
 * @type {HTMLElement} max_token_length_input - Input element for the maximum token length.
 * @type {HTMLElement} warning_message_analysis_frame_rate - Element for the warning message for analysis frame rate.
 * @type {HTMLElement} warning_message_max_token - Element for the warning message for maximum token length.
 **/
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
prompt_input = document.getElementById('prompt-input')
max_token_length_input = document.getElementById('max-token-length-input')
warning_message_analysis_frame_rate = document.getElementById('warning-message-analysis-frame-rate')
warning_message_max_token = document.getElementById('warning-message-max-token')


/* 
* @type {string} video_file_name - Name of the video file.
* @type {number} duration - Duration of the video in seconds.
* @type {number} fps - Frame rate of the video.
* @type {number} frame_count - Total number of frames in the video.
* @type {number} frame_rate - Frame rate for analysis.
* @type {number} total_frames_to_be_analyzed_var - Total frames to be analyzed.
* @type {boolean} warning_max_token_bool - Flag for maximum token length warning.
* @type {boolean} warning_analysis_frame_rate_bool - Flag for analysis frame rate warning.
*/
var video_file_name = "";
var duration = 0;
var fps = 0;
var frame_count = 0;
var frame_rate = 0;
var total_frames_to_be_analyzed_var = 0;
var warning_max_token_bool = false;
var warning_analysis_frame_rate_bool = true;

/**
 * Handles the video file load event, sends the file to the server, and updates the UI with video details.
 */
document.getElementById('load-video').onchange = function() {
    const video_file = this.files[0];
    video_file_name = this.files[0].name;
    
    if (!video_file) {
        alert("No file selected");
        return;
    }

    let formData = new FormData();
    formData.append("video_file", video_file);

    // Send the video file to the server
    fetch("/load-video", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Update the UI with video details
        duration = data.duration;
        fps = data.fps;
        frame_count = data.frame_count;
        const hours = Math.floor(data.duration / 3600);
        const minutes = Math.floor((data.duration % 3600) / 60);
        const seconds = Math.floor(data.duration % 60);
        video_length_label.innerHTML = `Video length : ${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        video_frame_rate_label.innerHTML = "Fps : " + data.fps;
        total_frames_label.innerHTML = "Total frames : " + data.frame_count;
        compute_total_frames_to_analyze();
    })
    .catch(error => console.error('Error:', error));

};

/**
 * Computes the total frames to be analyzed based on the frame rate input and updates the UI.
 */
function compute_total_frames_to_analyze() {
    frame_rate = frame_rate_input.value;
    total_frames_to_be_analyzed_var = Math.ceil(duration * frame_rate / 60);
    total_frames_to_be_analyzed.innerHTML = Math.max(total_frames_to_be_analyzed_var,0) + " frames";
    if (frame_rate / 60 > fps) {
        warning_message_analysis_frame_rate.textContent = "Warning: the analysis frame rate is higher than the video frame rate.";
        warning_analysis_frame_rate_bool = true;
        manage_start_transcription_button_availability()
    } else {
        warning_message_analysis_frame_rate.textContent = "";
        warning_analysis_frame_rate_bool = false;
        manage_start_transcription_button_availability()
    }
    if (frame_rate <= 0) {
        warning_message_analysis_frame_rate.textContent = "Warning: the frame rate must be positive.";
        warning_analysis_frame_rate_bool = true;
        manage_start_transcription_button_availability()
    }
}


/**
 * Manages the availability of the start transcription button based on warnings.
 */
function manage_start_transcription_button_availability() {
    if (warning_max_token_bool || warning_analysis_frame_rate_bool) {
        start_transcription.disabled = true;
    } else {
        start_transcription.disabled = false;
    }
}


/**
 * Displays a warning message if the maximum token length input is invalid.
 */
function display_warning_message_max_token() {
    if (max_token_length_input.value <= 0) {
        warning_message_max_token.textContent = "Warning: the maximum token length cannot be negative or zero.";
        warning_max_token_bool = true;
        manage_start_transcription_button_availability()
    } else {
        warning_message_max_token.textContent = "";
        warning_max_token_bool = false;
        manage_start_transcription_button_availability()
    }
}

// Add event listeners to ensure the UI is updated based on user input, and display warnings if necessary.
frame_rate_input.addEventListener('input', compute_total_frames_to_analyze);
max_token_length_input.addEventListener('input', display_warning_message_max_token);


/**
 * Handles the start transcription button click event, initiates the transcription process, and updates the UI with progress.
 */
start_transcription.onclick = function() {

    // Display loading bar
    loading_container.style.display = 'block';
    const excepted_frames = total_frames_to_be_analyzed_var
    var frame_received = 0;
    generated_frames.innerHTML = frame_received + "/" + excepted_frames + " frames";
    prompt = prompt_input.value;
    max_token_length = max_token_length_input.value;

    // Define the url for the event source
    const url = `/start-transcription?video_file_name=${encodeURIComponent(video_file_name)}&frame_rate=${encodeURIComponent(frame_rate)}&prompt=${encodeURIComponent(prompt)}&max_token_length=${encodeURIComponent(max_token_length)}`;

    // Create the event source
    const eventSource = new EventSource(url);
    eventSource.onmessage = function(event) {
        // replace '' by "" in event.data string
        const data = JSON.parse(event.data.replace(/'/g, "\""));
        const frame_id = data.frame_id;
        // Increment the number of frames received
        frame_received += 1;

        // Replace guillemetsimple and guillemetdouble by ' and " in the answer
        const answer = data.answer.replaceAll("guillemetsimple", "'").replaceAll("guillemetdouble", '"');

        // compute the timestamp
        const frameTime = frame_id / fps;
        const hours = Math.floor(frameTime / 3600);
        const minutes = Math.floor((frameTime % 3600) / 60);
        const seconds = Math.floor(frameTime % 60);
        const timestamp = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

        // Create the div element
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

        // Update the loading bar
        const percentage = Math.floor((frame_received / excepted_frames) * 100);
        loading_bar.style.width = percentage + "%";
        loading_percentage.innerHTML = percentage + "%";
        generated_frames.innerHTML = frame_received + "/" + excepted_frames + " frames";

        // Close the event source if the percentage is 100
        if (percentage == 100) {
            eventSource.close();
            loading_container.style.display = 'none';
        }
    };
    // Close the event source if an error occurs
    eventSource.onerror = function() {
        eventSource.close();
    };
};
