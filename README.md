My first venture into mcp servers.


Contains a tarot deck and three tools. Supports a single user, since the deck is fixed, once shuffled.

get_next_card() - for when you just want one. description optional.

celtic_cross_next() - gets the next card for a celtic cross reading. this includes the position on the cross, and a description of the card.

reset() - shuffle the deck again and reset the celtic cross

Cards may come with description. It felt right to shuffle the deck before use.

card descriptions (card_data.json) were borrowed from this repository: https://github.com/ekelen/tarot-api (No license, but: "You are welcome to just grab the JSON file that serves as the data source and use it for your own projects."). Notes: Changed "Fortitude" to "Strength". "The Last Judgment" to "Judgement".

By default, listens to 127.0.0.1:8000/tarot-mcp (if you're coming from localhost, replace 127.0.0.1 with localhost or you get a 403)

<img width="808" height="500" alt="image" src="https://github.com/user-attachments/assets/7cb79e95-f50d-4cd2-8242-da3b43cd6bde" />
Qwen 3.6 35B-A3B, in koboldcpp
