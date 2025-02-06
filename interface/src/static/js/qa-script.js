// get send-button element
var send_button = document.getElementById('send-button');

// get question-input element
var question_input = document.getElementById('question-input');

// get question-list element (main-content)
var main_content = document.getElementById('main-content');

// get the file from the input
var load_transcription = document.getElementById('load-transcription');

var thread = "";

// add click event listener to send-button
send_button.addEventListener('click', async function() {
    // get question from question-input
    var question = question_input.value;

    // check if input is not null or empty
    if (question.trim() !== '') {
        // create new question element
        var questionElement = document.createElement('div');
        questionElement.className = 'bg-white p-4 rounded-lg shadow-md self-end ml-auto max-w-lg';

        // create sender name element
        var senderName = document.createElement('p');
        senderName.className = 'text-gray-700 font-semibold';
        senderName.textContent = 'You';

        // create question text element
        var questionText = document.createElement('p');
        questionText.className = 'text-gray-600';
        questionText.textContent = question;
        thread += " Question from the user: " + question;

        // append sender name and question text to question element
        questionElement.appendChild(senderName);
        questionElement.appendChild(questionText);

        // append question element to main content
        main_content.appendChild(questionElement);

        // clear question-input
        question_input.value = '';

        // disable send-button
        send_button.disabled = true;

        // define prompt :

        // get the text from the text file input
        var context = "The following is a sequence of frame descriptions of a video. ================================================================================================================================== \n START OF VIDEO \n ";
        var file = await load_transcription.files[0].text();
        console.log(file);
        var pre_prompt = " \n END OF VIDEO \n ================================================================================================================================== \n You are an expert AI that can answer questions about the text you have read. Based on the text you just read, answer the last question. \n ";
        var post_question = " Use only fact from the text you have read, if you cannot find the answer, say 'I don't know'. The answer to the question is: ";
        var prompt = context + file + pre_prompt + thread + post_question;
        console.log(prompt);
        
        // fetch the answer from the server (send prompt to the server)
        fetch('/qa-answer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                prompt: prompt,
            }),
        }).then(response => response.json())
        .then(function(data) {
            // create new answer element
            thread += " Answer from the AI: " + data.answer;
            console.log(data.answer);

            // create new answer element
            var answerElement = document.createElement('div');
            answerElement.className = 'bg-blue-100 p-4 rounded-lg shadow-md self-start mr-auto max-w-lg';

            // create bot name element
            var botName = document.createElement('p');
            botName.className = 'text-gray-700 font-semibold';
            botName.textContent = 'Bot';

            // create answer text element
            var answerText = document.createElement('p');
            answerText.className = 'text-gray-600';
            answerText.textContent = data.answer;

            // append bot name and answer text to answer element
            answerElement.appendChild(botName);
            answerElement.appendChild(answerText);

            // append answer element to main content
            main_content.appendChild(answerElement);

            // enable send-button
            send_button.disabled = false;

        }).catch(error => console.error('Error:', error));

    }
});

// add event on change to question-input and enable send-button if input is not empty
question_input.addEventListener('input', function() {
    if (question_input.value.trim() !== '') {
        send_button.disabled = false;
    } else {
        send_button.disabled = true;
    }
});


