function sendFavorite(source, url) {
    fetch(url)
    .then(resp => resp.json())
    .then(json => {
        if (json.message === "Favorite Added!") {
            source.textContent = `${json.numLikes} favorites`;
        }
        alert(json.message);
    })
}