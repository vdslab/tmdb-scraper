const fetch = require("node-fetch");

const msec = 1000;

const API_KEY = process.env.API_KEY;
const baseUrl = "https://api.themoviedb.org/3/movie";

const sleep = (msec) =>
  new Promise((resolve) =>
    setTimeout(() => {
      resolve();
    }, msec)
  );

const getMovieCredits = async (id) => {
  const params = new URLSearchParams();
  params.set("api_key", API_KEY);
  params.set("language", "ja-JP");

  const reqUrl = `${baseUrl}/${id}/credits?${params.toString()}`;

  const res = await fetch(reqUrl);
  const data = await res.json();

  return data;
};

const getMoviesCredits = async (movies) => {
  const a = [];
  for (const d of movies) {
    await sleep(msec);
    const data = await getMovieCredits(d.id);
    console.log(data.id);
    a.push(data);
  }

  return a;
};

const main = async (movies) => {
  const data = await getMoviesCredits(movies);

  return data;
};

module.exports = main;
