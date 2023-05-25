// Get HTML elements
const burgerMenu = document.getElementById("burger-menu");
const burgerBtn = document.getElementById("burg-btn");
const burgerCloseBtn = document.getElementById("burg-btn-close");
const windowOuterWidth = window.outerWidth;
const popupBlock = document.querySelector(".popups");
const contactsBlock = document.querySelector(".contacts_block");
const aboutUsBlock = document.querySelector(".aboutus_block");
const contactsBtn = document.querySelector("#Contacts");
const aboutUsBtn = document.querySelector("#AboutUs");
const cartBtn = document.querySelector(".cart_btn");
const cartWrapper = document.querySelector(".cart_wrapper");
const cartBlock = document.querySelector(".cart_block");


// Burger menu dynamic
burgerBtn.addEventListener("click", function() {
    burgerMenu.style.display = "flex";
    burgerCloseBtn.style.display = "block";
    burgerBtn.style.display = "none";
});

burgerCloseBtn.addEventListener("click", function() {
    burgerMenu.style.display = "none";
    burgerBtn.style.display = "flex";
    burgerCloseBtn.style.display = "none";
});

window.addEventListener('resize', function(){
    let w = document.documentElement.clientWidth;
    let h =  document.documentElement.clientHeight;

    if (w > 912){
        burgerBtn.style.display = "none";
        burgerCloseBtn.style.display = "none";
        burgerMenu.style.display = "none";
    }
    else if (w < 912 && $('#burg-btn-close').css('display') == "block"){
        burgerBtn.style.display = "none";
    }
    else if (w < 912 && $('#burg-btn-close').css('display') == "none"){
        burgerBtn.style.display = "flex";
    }
});

// Popup dynamic

const contactsPopUp = document.querySelector(".contactsPopUp-wrapper")
const aboutusPopUp = document.querySelector(".aboutusPopUp-wrapper")

const popup_item = document.querySelectorAll(".popup_item")
var body = document.getElementsByTagName('body')[0];
contactsBtn.addEventListener("click", () => {
    contactsPopUp.classList.remove("popUphidden")
    contactsPopUp.classList.add("popUpshown")


    body.style.overflow = 'hidden';
   
    document.body.scrollTop = 0; // Для Safari
    document.documentElement.scrollTop = 0; // Для Chrome, Firefox, IE and Opera
  
})
contactsPopUp.addEventListener("click", () => {
    contactsPopUp.classList.remove("popUpshown")
    contactsPopUp.classList.add("popUphidden")

    body.style.overflow = 'visible';
})

aboutUsBtn.addEventListener("click", () => {
    aboutusPopUp.classList.remove("popUphidden")
    aboutusPopUp.classList.add("popUpshown")
    document.body.scrollTop = 0; // Для Safari
    document.documentElement.scrollTop = 0; // Для Chrome, Firefox, IE and Opera
    body.style.overflow = 'hidden';
   
   
})

aboutusPopUp.addEventListener("click", () => {
    aboutusPopUp.classList.remove("popUpshown")
    aboutusPopUp.classList.add("popUphidden")
    body.style.overflow = 'visible';
})
contactsPopUp.addEventListener("mouseover", (e) => {
    if (!e.target.closest(".contactsPopUp-block")) {
        contactsPopUp.classList.add("popUpHover")
    }
    if (e.target.closest(".contactsPopUp-block")) {
        contactsPopUp.classList.remove("popUpHover")
    }
});
aboutusPopUp.addEventListener("mouseover", (e) => {
    if (!e.target.closest(".aboutusPopUp-block")) {
        aboutusPopUp.classList.add("popUpHover")
    }
    if (e.target.closest(".aboutusPopUp-block")) {
        aboutusPopUp.classList.remove("popUpHover")
    }
});


function removeObjectAndShiftIds(arr, idToRemove) {
    
    const indexToRemove = arr.findIndex(obj => obj.id === idToRemove);
    

    arr.splice(indexToRemove, 1);
    
 
    for (let i = indexToRemove; i < arr.length; i++) {
      arr[i].id = i;
    }
    
    return arr;
  }
// Basket dynamic

let renderCart = () => {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    const cartBody = document.querySelector("ul.cart_item_list");
    cartBody.innerHTML = "";
    cart.forEach(element => {
        const div = document.createElement("div");
        div.setAttribute("id", element["id"]);
        div.innerHTML = `
            <li class="cart_item">
                <div><img class="cart_ProductImg" src=${element["img"]}></div>
                <div class="cart_ProductName">${element["name"]}</div>
                <div class="cart_ProductPrice" id="cart_item-price">${parseInt(element["price"])} p.</div>
                <div class="cart_ProductDeletBtn"> X </div>
            </li>
        `;
        cartBody.appendChild(div);
    });
    const totalPriceContent = document.querySelector(".total_price_content");
    const itemsPrices = document.querySelectorAll("#cart_item-price");
    let sum = 0;
    const cropStr = str => str.replace(/\D+/g, '');
    itemsPrices.forEach(e => {
        sum += Number(parseInt(`${e.innerHTML}`));
    });
    totalPriceContent.innerText = `Сумма: ${sum} p.`;
    let cartProductDeletBtn = document.querySelectorAll(".cart_ProductDeletBtn")
    cartProductDeletBtn.forEach((e, i) => {
        e.addEventListener("click", (event) => {
            event.stopPropagation()
            let cart = JSON.parse(localStorage.getItem('cart')) || [];
            removeObjectAndShiftIds(cart, i)
            localStorage.setItem('cart', JSON.stringify(cart));
            renderCart()
            // e.parentNode.remove()
        })
        
    })
}

cartBtn.addEventListener("click", () => {
    cartWrapper.classList.remove("hidden")
    cartWrapper.classList.add("shown")
    document.querySelector("body").style.overflow = "hidden"
    document.body.scrollTop = 0; // Для Safari
    document.documentElement.scrollTop = 0; // Для Chrome, Firefox, IE and Opera
    renderCart()
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    console.log(cart)
    
});

cartWrapper.addEventListener("mouseover", (e) => {
    if (!e.target.closest(".cart_block")) {
        cartWrapper.classList.add("hover")
    }
    if (e.target.closest(".cart_block")) {
        cartWrapper.classList.remove("hover")
    }
});
cartWrapper.addEventListener("click", (e) => {
    if (!e.target.closest(".cart_block")) {
        cartWrapper.classList.remove("shown")
        cartWrapper.classList.add("hidden")
       
        body.style.overflow = 'visible';
    }
});

