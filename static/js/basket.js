window.onload = () => {
    // Retrieve cart from local storage or create a new one
    function getTableSize() {
        const selectElement = document.querySelector("select#SizeSelect");
        if (selectElement !== null) {
            const pattern = /Цена за (\d+mm)/;
            return selectElement.querySelector(`option[value="${selectElement.value}"]`).innerHTML.match(pattern)[1];
        } else {
            return null;
        }
    };
    function getGridSize() {
        const GridSize = document.querySelector("select#GridSize")
        if (GridSize !== null) {
            if(GridSize.querySelector(`option[value="${GridSize.value}"]`).innerHTML.includes('-') === true){
                return GridSize.querySelector(`option[value="${GridSize.value}"]`).innerHTML.split("-")[1].trim();
            }
            
        } else {
            return null;
        }
    };
    function getAssembly() {
        const getAssembly = document.querySelector("select#assembly")
        if (getAssembly !== null) {
            return getAssembly.querySelector(`option[value="${getAssembly.value}"]`).innerHTML;
        } else {
            return null;
        }
    
    };
    function getLegs() {
        const getLegs = document.querySelector("select#legs")
        if (getLegs !== null) {
            return getLegs.querySelector(`option[value="${getLegs.value}"]`).innerHTML;
        } else {
            return null;
        }
    
    };
    // Add event listener to 'Add to Basket' button
    const addToBasketBtn = document.querySelector("a.buy-button");
    addToBasketBtn.addEventListener('click', () => {
        const cart = JSON.parse(localStorage.getItem('cart')) || [];
        const productName = document.querySelector("div.product-title").innerHTML;
        const productPrice = document.querySelector("div.product-price").innerHTML;
        const productImg = extractImageUrl(document.querySelector("div.product-picture").getAttribute("style"));
        const type = getType();
        
        cart.push({
            id: cart.length,
            type: type,
            img: productImg,
            name: productName,
            tableSize: getTableSize() || "no" ,
            tableGrid: getGridSize() || "no",
            price: parseInt(productPrice),
            Assembly: getAssembly(),
            Legs: getLegs(),
            quantity: 1,
        });
        // Save updated cart to local storage and render it
        localStorage.setItem('cart', JSON.stringify(cart));
    });

    // Extract the product type from the URL
    function getType() {
        const fullUrl = window.location.href;
        return getSecondSegment(fullUrl);
    }

    // Get the second segment of a URL
    function getSecondSegment(url) {
        const segments = url.split('/');
        return segments[3]; // index 3 corresponds to the second segment
    }

    // Extract the URL of a background image from a CSS string
    const extractImageUrl = cssString => {
        const match = cssString.match(/url\(['"]?([^'"]+)['"]?\)/);
        return match ? match[1] : null;
    };
};


//valid phone number
function formatTel(input) {
    var value = input.value;
    value = value.replace(/\D/g,''); 
    if (!value.startsWith('7')) value = '7' + value; 
    value = value.substring(0, 11);
    var output = `+${value.replace(/(\d{1})(\d{3})(\d{3})(\d{4})/,"7($2)$3-$4")}`; 
    input.value = output;
  }

  
// PopUps
