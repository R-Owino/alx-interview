## Star Wars API

The problem:
```
Print all characters of a Star Wars movie
```

Problem instructions:
- The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
- Display one character name per line in the same order as the “characters” list in the /films/ endpoint
- You must use the [Star wars ](https://swapi-api.alx-tools.com/) API
- You must use the request module

Create the environment:
- Install Node 10
```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

- Install semistandard
```
$ sudo npm install semistandard --global
```

- Install `request` module
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

Run the file:
```node 0-starwars_characters.js 3```

Output:
```
remmy@remmy:~/alx-interview/0x06-starwars_api$ node 0-starwars_characters.js 3
Obi-Wan Kenobi
C-3PO
Luke Skywalker
R2-D2
Leia Organa
Darth Vader
Jabba Desilijic Tiure
Wedge Antilles
Han Solo
Chewbacca
Yoda
Boba Fett
Lando Calrissian
Palpatine
Mon Mothma
Arvel Crynyd
Ackbar
Bib Fortuna
Wicket Systri Warrick
Nien Nunb
```
