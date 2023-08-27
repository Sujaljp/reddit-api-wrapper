const articlesContainer = document.getElementById("articles-container");

async function fetchArticles(url) {
    articlesContainer.innerHTML = "<h1>Loading...</h1>"
    try {
        const response = await fetch("http://127.0.0.1:8000/"+url);
        const threads = await response.json();
        articlesContainer.innerHTML = ""
        
        threads.forEach(article => {

            const date = (new Date(article.created*1000)).toDateString();
            const articleDiv = document.createElement("div");
            articleDiv.classList.add("article");
            articleDiv.innerHTML = `
                <div class="card">
                    <h3>${article.title}</h3>
                    <div class="description">
                        <span>Author: ${article.author}</span>
                        <span>Posted: ${date}</span>
                        <a href="${article.url}" target="_blank">Open Post</a>
                    </div>
                </div>
            `;

            articlesContainer.appendChild(articleDiv);
        });
    } catch (error) {
        console.error("Error fetching articles:", error);
    }
}

fetchArticles("new");



