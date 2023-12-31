from flask import Flask, render_template

articles = [
	{ "art_id": 1,
      "art_img_link": "https://shorturl.at/jnzC0",
	  "art_title": "Learn Html For Free", 
	  "art_desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi quis leo purus.",
      "art_topic": "Programming"
    },

    { "art_id": 2,
      "art_img_link": "https://shorturl.at/crQTV",
	  "art_title": "Roadmap For CyberSecurity", 
	  "art_desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi quis leo purus.",
      "art_topic": "Hacking"
    },

    { "art_id": 3,
      "art_img_link": "https://shorturl.at/lnprC",
	  "art_title": "5 Tips To Master JS", 
	  "art_desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi quis leo purus.",
      "art_topic": "Programming"
    },

    { "art_id": 4,
      "art_img_link": "https://shorturl.at/gijk9",
	  "art_title": "Learn Flask For Free", 
	  "art_desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi quis leo purus.",
      "art_topic": "Programming"
    }
]

myblog = Flask(__name__)

@myblog.route("/")
def index():
	return render_template("index.html", articles = articles)

myblog.run(debug=True)