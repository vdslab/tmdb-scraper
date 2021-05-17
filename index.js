const fs = require("fs");
require("dotenv").config();

const getMovies = require("./getMovies");
const getMoviesDetails = require("./getMoviesDetails");
const getMoviesCredits = require("./getMoviesCredits");

const FROM = 2014;
const TO = 2016;

const writeJSON = (path, data) => {
  fs.writeFileSync(path, JSON.stringify(data));
};

const main = async () => {
  for (let year = FROM; year <= TO; ++year) {
    const moviesPath = `./data/${year}/JP_MOVIES.json`;
    const moviesDetailsPath = `./data/${year}/JP_DETAILS.json`;
    const moviesCreditsPath = `./data/${year}/JP_CREDITS.json`;

    const movies = await getMovies(year);
    writeJSON(moviesPath, { data: movies });

    const moviesDetails = await getMoviesDetails(movies);
    writeJSON(moviesDetailsPath, { data: moviesDetails });

    const moviesCredits = await getMoviesCredits(movies);
    writeJSON(moviesCreditsPath, { data: moviesCredits });
  }
};

main();
