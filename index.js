const fs = require("fs");

const getMovies = require("./getMovies");
const getMoviesDetails = require("./getMoviesDetails");
const getMoviesCredits = require("./getMoviesCredits");

const YEAR = 2021;

const moviesPath = `./data/${YEAR}/JP_MOVIES.json`;
const moviesDetailsPath = `./data/${YEAR}/JP_DETAILS.json`;
const moviesCreditsPath = `./data/${YEAR}/JP_CREDITS.json`;

const writeJSON = (path, data) => {
  fs.writeFileSync(path, JSON.stringify(data));
};

const main = async () => {
  const movies = await getMovies(YEAR);
  writeJSON(moviesPath, { data: movies });

  const moviesDetails = await getMoviesDetails(movies);
  writeJSON(moviesDetailsPath, { data: moviesDetails });

  const moviesCredits = await getMoviesCredits(movies);
  writeJSON(moviesCreditsPath, { data: moviesCredits });
};

main();
