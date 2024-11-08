from flask import Flask, render_template, request, jsonify
 import openai
 
 app = Flask(__name__)
 
 # Set your OpenAI API key
 openai.api_key = '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'
 
 @app.route("/")
 def index():
     return render_template("index.html")
 
 @app.route("/get", methods=["GET", "POST"])
 def get_bot_response():
     if request.method == "POST":
         user_message = request.form["msg"]
         
         # Send user input to OpenAI GPT model
         response = openai.Completion.create(
             engine="text-davinci-003",  # You can also use other models like "gpt-3.5-turbo"
             prompt=user_message,
             max_tokens=150,
             temperature=0.7
         )
         
         # Extract the reply text from OpenAI's response
         bot_reply = response.choices[0].text.strip()
         
         return jsonify({"response": bot_reply})
     return jsonify({"response": "I'm sorry, I didn't understand that."})
 
 if __name__ == "__main__":
     app.run(debug=True)
 
