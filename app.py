from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Happy Birthday, Ate! 💕</title>

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;

            background: linear-gradient(
                135deg,
                #eadcff,
                #f8e1ff,
                #dff4ff
            );

            overflow-x: hidden;
        }

        .heart {
            position: fixed;
            font-size: 25px;
            animation: float 6s infinite ease-in-out;
            opacity: 0.7;
        }

        .h1 { left: 8%; top: 80%; }
        .h2 { left: 85%; top: 70%; animation-delay: 1s; }
        .h3 { left: 15%; top: 30%; animation-delay: 2s; }
        .h4 { left: 75%; top: 20%; animation-delay: 3s; }

        @keyframes float {
            0% {
                transform: translateY(0) rotate(0deg);
            }

            50% {
                transform: translateY(-80px) rotate(15deg);
            }

            100% {
                transform: translateY(0) rotate(-15deg);
            }
        }

        .card {
            width: 90%;
            max-width: 430px;
            padding: 30px 25px;
            text-align: center;

            background: rgba(255,255,255,0.94);

            border-radius: 30px;

            box-shadow:
                0 15px 40px rgba(150, 80, 120, 0.25);

            position: relative;
            z-index: 2;
        }

        .photo {
            width: 190px;
            height: 190px;

            object-fit: cover;

            border-radius: 50%;

            border: 7px solid white;

            box-shadow:
                0 8px 25px rgba(200, 80, 130, 0.3);

            margin-bottom: 15px;
        }

        .birthday {
            font-size: 45px;
            margin: 5px;
        }

        h1 {
            color: #d85b91;
            font-size: 30px;
            margin: 10px 0;
        }

        .subtitle {
            color: #666;
            font-size: 16px;
            margin-bottom: 20px;
        }

        button {
            border: none;
            background: linear-gradient(
                135deg,
                #ec76a9,
                #d95791
            );

            color: white;

            padding: 13px 28px;

            border-radius: 30px;

            font-size: 16px;

            cursor: pointer;

            box-shadow: 0 6px 15px rgba(210,80,130,0.3);
        }

        button:hover {
            transform: scale(1.05);
        }

        #message {
            display: none;

            margin-top: 25px;

            padding: 20px;

            background: #fff1f7;

            border-radius: 20px;

            color: #555;

            line-height: 1.7;

            animation: appear 0.6s ease;
        }

        @keyframes appear {
            from {
                opacity: 0;
                transform: translateY(15px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .love {
            color: #d95791;
            font-weight: bold;
        }

        @media (max-width: 480px) {

            .card {
                padding: 25px 18px;
            }

            .photo {
                width: 160px;
                height: 160px;
            }

            h1 {
                font-size: 26px;
            }
        }
    </style>
</head>

<body>

    <!-- Floating hearts -->

    <div class="heart h1">💗</div>
    <div class="heart h2">💗</div>
    <div class="heart h3">💗</div>
    <div class="heart h4">😊</div>
    <div class="heart h5">😍</div>
    <div class="heart h6">🥰</div>
    <div class="heart h7">💗</div>
    <div class="heart h8">💗</div>
    <div class="heart h9">💗</div>
            

    


    <!-- Birthday Card -->

    <div class="card">

        <!-- YOUR ATE'S PHOTO -->
        <img
            src="/static/ate.jpg"
            class="photo"
            alt="My Ate"
        >

        <div class="birthday">🎂</div>

        <h1>
            Happy Birthday, Ate! 💕
        </h1>

        <p class="subtitle">
            I made this little surprise just for you. 🌸
        </p>

        <button onclick="openMessage()">
            Open My Message 💌
        </button>


        <!-- YOUR PERSONAL MESSAGE -->

        <div id="message">

            <p>
                Happy Birthday to my wonderful Ate! 🎂💕
            </p>

            <p>
                 Thank you so much for always supporting me, 
                 especially in my studies. 
                 Your sacrifices, encouragement, and help mean so much to me.
                   I'm truly blessed to have a sister like you. I
                     promise to do my best and make you proud. I love you so much, Ate! 🥹❤️ 
                     May you have a wonderful birthday and many more blessings to come! 🎉🎂
            </p>


            <p>
                You deserve all the good things in life.
            </p>

            <p class="love">
                I love you so much, Ate Buda! ❤️
            </p>

            <p>
                Enjoy your special day! 🥳🌸🎂
            </p>

        </div>

    </div>


    <script>

        function openMessage() {

            var message = document.getElementById("message");

            if (message.style.display === "block") {

                message.style.display = "none";

            } else {

                message.style.display = "block";

            }

        }

    </script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(debug=True)