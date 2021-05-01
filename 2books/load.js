
        async function load(path) {
            const img = document.getElementById("book-image");
            const author = document.getElementById("author");
            const title = document.getElementById("title");
            const parent = document.getElementById("parent");

            let card = document.createElement("div")
            card.setAttribute("class", "card")


            let result = await fetch("http://localhost:3333/" + path);
            
            if (result.ok) {

                const data = await result.json();
                
                if (data) {
                    data.forEach(d => {
      

                  console.log(d);

        cc = '<div class="card" style="width: 19rem;">\
            <img src="../2books/image/' + d["book-image"] + '" class="card-img-top">\
            <div class="card-body">\
                <div class="card-header">\
                    <h4 class="card-title">'
                        + d["title"] +
                    '</h4></div><p>'
                        + d["author"] +
                '</p></div></div>';
                        

                        console.log(d);
                        //cc = '<div style="width:30%">' + d["author"] + '<br/>' + d["title"]+ ' </div><br /><br />';
                        parent.innerHTML += cc;
                    });
                }
            } else {
                alert("no data")
            }
        }
  
