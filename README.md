### Content Based Article Recommender Engine


The goal of this project is to make a simple article recommendation engine using a natural language processing technique called word2vec. word2vec is an algorithm for constructing vector representations of words, also known as word embeddings. In particular, we're going to use a "database" from Stanford's GloVe project trained on a dump of Wikipedia.

Around the recommendation engine, I'm going to build a web server that displays a list of BBC articles. Clicking on one of those articles takes you to an article page that shows the text of the article as well as a list of five recommended articles.


Usage: run server.py will launch the server for recommender engine.

Data: Glove database as well as BBC articles are not included due to size problems.