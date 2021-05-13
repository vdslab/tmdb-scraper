const fetch = require("node-fetch");

const msec = 1000;

const API_KEY = process.env.API_KEY;
const baseUrl = "https://api.themoviedb.org/3/discover/movie";

const sleep = (msec) =>
  new Promise((resolve) =>
    setTimeout(() => {
      resolve();
    }, msec)
  );

const getPage = async (page, params) => {
  params.set("page", page);
  const reqUrl = `${baseUrl}/?${params.toString()}`;
  const res = await fetch(reqUrl);
  const data = await res.json();

  return data;
};

const getMovies = async (year) => {
  const a = [];
  const params = new URLSearchParams();
  params.set("api_key", API_KEY);
  params.set("language", "ja-JP");
  params.set("region", "JP");
  params.set("sort_by", "release_date.asc");
  params.set("include_adult", false);
  params.set("include_video", false);
  params.set("page", 1);
  params.set("release_date.gte", `${year}-01-01`);
  params.set("release_date.lte", `${year}-12-31`);
  params.set("with_watch_monetization", "flatrate");

  const firstPageData = await getPage(1, params);
  a.push(...firstPageData.results);
  console.log(firstPageData.page);

  const totalPages = firstPageData.total_pages;
  for (let page = 2; page <= totalPages; ++page) {
    await sleep(msec);
    const pageData = await getPage(page, params);
    console.log(pageData.page);
    a.push(...pageData.results);
    if (page === 2) break;
  }

  return a;
};

const main = async (year) => {
  const data = await getMovies(year);

  return data;
};

module.exports = main;
