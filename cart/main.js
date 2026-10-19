
let products = [
    {
        id: 1,
        name: "Book",
        price: 3000,
        category: "stationery"
    },
    {
        id: 2,
        name: "iPhone 15",
        price: 350000,
        category: "smartphone"
    },
    {
        id: 3,
        name: "Smart TV",
        price: 250000,
        category: "electronics"
    },
    {
        id: 4,
        name: "Laptop",
        price: 500000,
        category: "electronics"
    },
    {
        id:5,
        name: "Standing Fan",
        price: 55000,
        category:"electronics"
    },
    {
        id:6,
        name:"Office Chair",
        price: 75000,
        category:"furniture"
    }
];

let productsdiv = document.getElementById('products');
let cartsdiv = document.getElementById('carts');
let cartsummary = document.getElementById('cart_summary');
let cartcountdiv = document.getElementById('cartcount');
let carts = [];

function fetchLocalStorageCart() {
    let cartInStorage = localStorage.getItem("carts");
    if (cartInStorage) {
        try {
            let storedCart = JSON.parse(cartInStorage);
            carts = Array.isArray(storedCart) ? storedCart : [];
        } catch (error) {
            carts = [];
        }
    }
}

function saveCart() {
    localStorage.setItem("carts", JSON.stringify(carts));
}

function displayProduct() {
    products.forEach(function (pro) {
        let proDiv = document.createElement("div");
        proDiv.classList.add("product");

        let proH2 = document.createElement("h2");
        proH2.textContent = pro.name;

        let proP = document.createElement("p");
        proP.textContent = "₦ " + pro.price.toLocaleString();

        let proBtn = document.createElement("button");
        proBtn.textContent = "Add to cart";
        proBtn.addEventListener("click", function () {
            addToCart(pro.id);
        });

        proDiv.append(proH2, proP, proBtn);
        productsdiv.append(proDiv);
    });
}

function addToCart(proId) {
    let productToCart = products.find(function (product) {
        return product.id === proId;
    });

    if (!productToCart) return;

    let productInCart = carts.find(function (cartItem) {
        return cartItem.id === proId;
    });

    if (productInCart) {
        productInCart.qty += 1;
    } else {
        carts.push({ ...productToCart, qty: 1 });
    }

    saveCart();
    renderCart();
    renderCartSummary();
}

function renderCart() {
    cartsdiv.innerHTML = "";

    if (carts.length === 0) {
        cartsdiv.textContent = "Your cart is empty.";
        renderCartSummary();
        return;
    }

    carts.forEach(function (cartItem) {
        let cartItemDiv = document.createElement("div");
        cartItemDiv.classList.add("cart-item-container");

        let productNameP = document.createElement("p");
        productNameP.textContent = cartItem.name;

        let productPriceP = document.createElement("p");
        productPriceP.textContent = "₦" + Number(cartItem.price).toLocaleString();

        let productDecBtn = document.createElement("button");
        productDecBtn.textContent = "-";
        productDecBtn.addEventListener("click", function () {
            decreaseCartQty(cartItem.id);
        });

        let productQtyP = document.createElement("p");
        productQtyP.textContent = cartItem.qty;

        let productIncBtn = document.createElement("button");
        productIncBtn.textContent = "+";
        productIncBtn.addEventListener("click", function () {
            increaseCartQty(cartItem.id);
        });

        let productPriceTotalP = document.createElement("p");
        productPriceTotalP.textContent = "Total: ₦ " + (Number(cartItem.price) * Number(cartItem.qty)).toLocaleString();

        cartItemDiv.append(productNameP, productPriceP, productDecBtn, productQtyP, productIncBtn, productPriceTotalP);
        cartsdiv.append(cartItemDiv);
    });
}

function increaseCartQty(id) {
    let product = carts.find(function (ct) {
        return ct.id === id;
    });

    if (!product) return;

    product.qty += 1;
    saveCart();
    renderCart();
    renderCartSummary();
}

function decreaseCartQty(id) {
    let product = carts.find(function (ct) {
        return ct.id === id;
    });

    if (!product) return;

    if (product.qty > 1) {
        product.qty -= 1;
    } else {
        carts = carts.filter(function (ct) {
            return ct.id !== id;
        });
    }

    saveCart();
    renderCart();
    renderCartSummary();
}

function renderCartSummary() {
    if (!cartsummary) return;

    cartsummary.innerHTML = "";

    let total = 0;
    carts.forEach(function (ct) {
        total += Number(ct.qty) * Number(ct.price);
    });

    let totalItems = carts.reduce(function (sum, item) {
        return sum + Number(item.qty);
    }, 0);

    let cartCount = document.createElement("p");
    cartCount.textContent = "Cart count: " + totalItems;

    let totalPrice = document.createElement("h3");
    totalPrice.textContent = "Total Price = ₦ " + total.toLocaleString();

    cartsummary.append(cartCount, totalPrice);

    if (cartcountdiv) {
        cartcountdiv.textContent = "Cart count: " + totalItems;
    }
}

fetchLocalStorageCart();
displayProduct();
renderCart();
renderCartSummary();