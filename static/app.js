const feature = document.getElementById("feature");

const inputLabel = document.getElementById("inputLabel");
const inputText = document.getElementById("inputText");

const quizOptions = document.getElementById("quizOptions");
const numberQuestions = document.getElementById("numberQuestions");

const learningOptions = document.getElementById("learningOptions");
const level = document.getElementById("level");
const goal = document.getElementById("goal");

const generateBtn = document.getElementById("generateBtn");
const loading = document.getElementById("loading");
const result = document.getElementById("result");


/* -----------------------------------------
   Update UI when feature changes
----------------------------------------- */

feature.addEventListener("change", function () {

    quizOptions.classList.add("hidden");
    learningOptions.classList.add("hidden");

    inputText.value = "";

    if (feature.value === "qa") {

        inputLabel.innerText = "Enter your question";
        inputText.placeholder = "Example: What is Python?";

    }

    else if (feature.value === "explain") {

        inputLabel.innerText = "Enter topic to explain";
        inputText.placeholder = "Example: Explain Binary Tree";

    }

    else if (feature.value === "quiz") {

        inputLabel.innerText = "Enter quiz topic";
        inputText.placeholder = "Example: Computer Networks";

        quizOptions.classList.remove("hidden");

    }

    else if (feature.value === "summarize") {

        inputLabel.innerText = "Enter text to summarize";
        inputText.placeholder =
            "Paste the text you want to summarize here...";

    }

    else if (feature.value === "learning_path") {

        inputLabel.innerText = "Enter learning topic";
        inputText.placeholder = "Example: Web Development";

        learningOptions.classList.remove("hidden");

    }

});


/* -----------------------------------------
   Escape HTML
----------------------------------------- */

function escapeHtml(text) {

    return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");
}


/* -----------------------------------------
   Simple Markdown Renderer
----------------------------------------- */

function renderMarkdown(text) {

    if (!text) {
        return "";
    }

    let html = escapeHtml(text);

    // Remove unnecessary escape characters
    html = html.replace(/\\([*_#`-])/g, "$1");

    // Code blocks
    html = html.replace(
        /```(?:python|javascript|html|css|json|text)?\n?([\s\S]*?)```/gi,
        '<pre><code>$1</code></pre>'
    );

    // Headings
    html = html.replace(
        /^### (.+)$/gm,
        "<h4>$1</h4>"
    );

    html = html.replace(
        /^## (.+)$/gm,
        "<h3>$1</h3>"
    );

    html = html.replace(
        /^# (.+)$/gm,
        "<h2>$1</h2>"
    );

    // Horizontal lines
    html = html.replace(
        /^---+$/gm,
        "<hr>"
    );

    // Bold
    html = html.replace(
        /\*\*(.*?)\*\*/g,
        "<strong>$1</strong>"
    );

    // Italic
    html = html.replace(
        /\*(.*?)\*/g,
        "<em>$1</em>"
    );

    // Bullet points
    html = html.replace(
        /^[*+-] (.+)$/gm,
        "• $1"
    );

    // Numbered lists
    html = html.replace(
        /^(\d+)\. (.+)$/gm,
        "$1. $2"
    );

    // Line breaks
    html = html.replace(/\n/g, "<br>");

    return html;
}


/* -----------------------------------------
   Generate Request
----------------------------------------- */

generateBtn.addEventListener("click", async function () {

    const selectedFeature = feature.value;
    const text = inputText.value.trim();


    /* Validation */

    if (!text) {

        result.innerHTML =
            '<p class="error-message">Please enter a question or topic.</p>';

        return;
    }


    loading.classList.remove("hidden");
    generateBtn.disabled = true;

    result.innerHTML = "Processing...";


    let url = "";
    let data = {};


    /* Q&A */

    if (selectedFeature === "qa") {

        url = "/qa";

        data = {
            text: text
        };
    }


    /* Explanation */

    else if (selectedFeature === "explain") {

        url = "/explain";

        data = {
            text: text
        };
    }


    /* Quiz */

    else if (selectedFeature === "quiz") {

        url = "/quiz";

        let questionCount =
            parseInt(numberQuestions.value);

        if (
            isNaN(questionCount) ||
            questionCount < 1
        ) {
            questionCount = 1;
        }

        if (questionCount > 20) {
            questionCount = 20;
        }

        data = {
            topic: text,
            number_of_questions: questionCount
        };
    }


    /* Summary */

    else if (selectedFeature === "summarize") {

        url = "/summarize";

        data = {
            text: text
        };
    }


    /* Learning Path */

    else if (selectedFeature === "learning_path") {

        url = "/learn/recommendations";

        data = {
            topic: text,
            level: level.value,
            goal: goal.value.trim() || "Learn the basics"
        };
    }


    /* Send request */

    try {

        const response = await fetch(url, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)

        });


        const responseData = await response.json();

        console.log("EduGenie API Response:", responseData);


        /* Successful response */

        if (
            response.ok &&
            responseData.success === true
        ) {

            result.innerHTML =
                renderMarkdown(responseData.result);

        }


        /* Backend error */

        else if (responseData.error) {

            result.innerHTML =
                '<p class="error-message"><strong>Error:</strong> ' +
                escapeHtml(responseData.error) +
                "</p>";

        }


        /* FastAPI validation error */

        else if (responseData.detail) {

            result.innerHTML =
                '<p class="error-message"><strong>Error:</strong> ' +
                escapeHtml(JSON.stringify(responseData.detail)) +
                "</p>";

        }


        else {

            result.innerHTML =
                '<p class="error-message">Something went wrong.</p>';

        }

    }


    catch (error) {

        console.error("Connection Error:", error);

        result.innerHTML =
            '<p class="error-message"><strong>Connection Error:</strong> ' +
            escapeHtml(error.message) +
            "</p>";

    }


    finally {

        loading.classList.add("hidden");
        generateBtn.disabled = false;

    }

});