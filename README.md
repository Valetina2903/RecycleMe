# RecycleMe
# Home Page
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RecycleMe</title>
    <link rel="stylesheet" href="css.css">
</head>
<body>
<header>
    <h1>RecycleMe</h1>
    <p>Find Recycling Points Near You</p>
</header>
<nav>
    <ul>
        <li><a href="Home.html">Home</a></li>
        <li><a href="ShopMe.html">ShopMe</a></li>
    </ul>
</nav>
<section class="animated-section">
    <h2>Welcome to RecycleMe</h2>
    <p>Start your recycling journey with us.</p>
</section>
<div class="square">
    <!-- News Section -->
    <div class="content section">
        <img src="news.jpg" alt="Latest Recycling News" class="section-image" width="150" height="100">
        <h3>Latest Recycling News</h3>
        <p>Get the latest updates on recycling trends and policies.</p>
        <a href="news.html">
            <button>Read News</button>
        </a>
    </div>
    <!-- Product Information Section -->
    <div class="content section">
        <img src="eco-friendly-products.jpg" alt="Product Information" class="section-image" width="150" height="100">
        <h3>Product Information</h3>
        <p>Discover the eco-friendliness of various products:</p>
        <a href="product_information.html">
            <button>View Product Information</button> <!-- Replaced the search with a single button -->
        </a>
    </div>
    <!-- Recycling Points Section -->
    <div class="content section">
        <img src="map_locator.jpg" alt="Recycling Points" class="section-image" width="150" height="100">
        <h3>Recycling Points</h3>
        <p>Find recycling points near your location to make recycling easier</p>
        <a href="nearest_recycling_point.html">
            <button type="button">Recycling Points</button>
        </a>
    </div>
</div>
</div>
<footer>
    <div class="green-part">
        <div class="contact-info">
            <p>Need Assistance?</p>
            <p>24/7 Support Available</p>
            <p>Contact Us: (+374) 00 000 000</p>
            <p>support@recycleme.io</p>
        </div>
    </div>
    <div class="copyright">
        <p>© 2024 RecycleMe. All Rights Reserved.</p>
    </div>
    <div class="social-icons">
        <a href="https://www.instagram.com" target="_blank">
            <img src="instagram.jpg" alt="instagram" width="30" height="30">
        </a>
        <a href="https://www.facebook.com" target="_blank">
            <img src="facebook1.jpg" alt="facebook"  width="30" height="30">
        </a>
        <a href="https://www.twitter.com" target="_blank">
            <img src="twitter1.png" alt="twitter"  width="30" height="30">
        </a>
    </div>
</footer>
<script src="script.js"></script>
</body>
</html>

# Css Home Page

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background-color: #E5E5E5; /* Light gray background color */
}

header {
    background-color: darkgreen;
    color: #d3d3d3;
    text-align: center;
    padding: 50px 0;
    background-image: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)), url("background.jpeg");
}

nav {
    background-color: #11400d; /* Green background color */
    text-align: center; /* Center-align the text */
}

nav ul {
    display: inline-block; /* Make the list items display inline */
    padding: 0;
}

nav ul li {
    display: inline;
    margin-right: 20px;
}

nav ul li a {
    color: #FFFFFF; /* White text color */
    text-decoration: none;
}

nav ul li a:hover {
    text-decoration: underline;
}

section {
    padding: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 10vh; /* Adjust the height as needed */
    flex-direction: column;
}

/* Add a smooth fade-in and slide-up animation to the text */
.animated-section {
    opacity: 0; /* Start with hidden text */
    transform: translateY(20px); /* Start with the text slightly below */
    animation: fadeInUp 1.5s ease-out forwards; /* Apply animation */
}

/* Define the keyframes for the animation */
@keyframes fadeInUp {
    0% {
        opacity: 0;
        transform: translateY(20px); /* Start below */
    }
    100% {
        opacity: 1;
        transform: translateY(0); /* End at normal position */
    }
}
/* Optional: add a slight delay to give a nice sequence */
.animated-section h2 {
    animation-delay: 0.2s; /* Delay for the title */
}

.animated-section p {
    animation-delay: 0.4s; /* Delay for the paragraph */
}

/* Container for the sections */
/* Container for the 3 sections (Apply green gradient border to this container) */
.square {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    flex-wrap: wrap; /* Allow sections to wrap if the screen is too small */
    border: 5px solid transparent; /* Transparent border for the container */
    background-image: linear-gradient(to right, #11400d, #0e3b07); /* Green gradient border */
    border-radius: 8px; /* Apply rounded corners to the container */
    padding: 20px; /* Padding between sections and the border */
    box-sizing: border-box;
}

/* Section styling inside the container */
.section {
    background-color: #ffffff; /* White background for the section */
    padding: 20px;
    margin: 10px;
    border-radius: 8px;
    width: 30%; /* Adjust the section width */
    box-sizing: border-box;
    position: relative;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Light shadow */
}

/* Section Image Styling */
.section img {
    max-width: 100%; /* Ensure the images are responsive */
    height: auto; /* Keep the aspect ratio */
    margin-bottom: 15px; /* Space between image and text */
}
/* Content inside sections */
.content {
    text-align: center;
}

/* Button styling */
button {
    background-color: #11400d;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: #0e3b07;
}

/* Section Image Styling */
.section-image {
    max-width: 100%;
    height: auto;
    margin-bottom: 10px;
}

/* Responsive Design for Smaller Screens */
@media (max-width: 768px) {
    .content {
        width: 100%; /* Stack sections on smaller screens */
    }
}

footer {
    background-color: #11400d;
    color: #d3d3d3;
    padding: 20px;
    margin-top: 100px;
    text-align: center;
}

.social-icons {
    display: flex;
    justify-content: center; /* Centers the icons */
    gap: 20px; /* Adds equal spacing between icons */
    margin-top: 10px; /* Optional: adds space above the icons */
}

.social-icons a img {
    display: block;
}


.green-part {
    background-color: #6BCD94;
    padding: 20px;
    text-align: center;
    background-image: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)), url("background.jpeg");
}

# Produrct information page

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Information</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #E5E5E5; /* Light gray background color */
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        header {
            background: url('background.jpeg') no-repeat center center/cover;
            color: #d3d3d3;
            height: 213.28px;
            width: 400px;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            font-family: 'Roboto', sans-serif;
            position: relative;
            box-sizing: border-box;
        }

        header h1 {
            position: relative;
            z-index: 1;
            font-size: 36px;
            margin: 0;
            font-weight: 600;
            color: #d3d3d3;
            text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
        }

        nav {
            background-color: #11400d; /* Green background color */
            text-align: center; /* Center-align the text */
            width: 100%; /* Ensure the nav takes up the full width of the page */
            padding: 15px 0; /* Increase the vertical padding for a more prominent nav */
        }

        nav ul {
            display: inline-block; /* Keep the list inline */
            padding: 0;
            margin: 0;
        }

        nav ul li {
            display: inline; /* Display list items inline */
            margin-right: 20px; /* Space between items */
        }

        nav ul li a {
            color: #FFFFFF; /* White text color */
            text-decoration: none; /* Remove underline */
            font-size: 16px; /* Font size consistent with your initial request */
        }

        nav ul li a:hover {
            text-decoration: underline; /* Underline on hover */
        }

        /* Hidden by default */
        #searchMessage {
            margin-top: 20px;
            font-size: 18px;
            color: #11400d;
            font-weight: bold;
            display: none; /* Initially hidden */
            opacity: 0; /* Hidden for fade-in effect */
            transition: opacity 0.5s ease-in-out; /* Smooth fade-in transition */
        }

        /* You can adjust the gap between the text and button if necessary */
        .search-section {
            text-align: center;
            margin-top: 10px; /* Reduced margin-top to move it up */
            padding: 55px;
        }
        .hidden {
            display: none;
        }

        #searchInput {
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        button {
            padding: 12px 20px;
            background-color: #11400d;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
        }

        .product-info {
            margin-top: 20px; /* Reduced margin-top to move it up */
            text-align: center;
            padding: 20px;
            background-color: rgba(255, 255, 255, 0.7); /* Transparent white background */
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 50px;
            border: 5px solid #11400d; /* Green border around the feature section */
        }

        .feature-container {
            display: flex; /* Aligns the child elements horizontally */
            justify-content: space-evenly; /* Evenly spaces the feature boxes */
            gap: 20px; /* Adds space between the boxes */
            flex-wrap: wrap; /* Allows the items to wrap into the next line on smaller screens */
        }

        .feature {
            background-color: #ffffff; /* White background for each feature box */
            padding: 20px;
            width: 250px; /* Adjust the width of each feature */
            text-align: center;
            border-radius: 10px; /* Rounded corners */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Optional shadow */
        }

        .feature img {
            width: 100px; /* Adjust the size of the images */
            height: 100px;
            margin-bottom: 10px; /* Adds space below the images */
        }

        .feature h4 {
            font-size: 20px; /* Title font size */
            margin: 10px 0; /* Margin around the title */
        }

        .feature p {
            font-size: 14px; /* Text size for descriptions */
        }

        footer {
            background-color: #11400d;
            color: #fff; /* White text color */
            padding: 20px;
            margin-top: auto;
            text-align: center;
            width: 100%;
        }

        footer p {
            margin: 5px 0;
        }

        footer .social-icons {
            position: relative;
            z-index: 10;  /* Ensure it’s above the overlay */
        }
        .search-section{
            padding: 55px;
        }
    </style>
</head>
<body>
<header>
    <h1>Product Information</h1>
</header>
<nav>
    <ul>
        <li><a href="start.html">Home</a></li>
        <li><a href="ShopMe.html">ShopMe</a></li>
    </ul>
</nav>
<div class="search-section">
    <h2>Search Product</h2>
    <form id="productSearchForm" onsubmit="searchProduct(event)">
        <input type="text" id="searchInput" placeholder="Enter barcode or product name...">
        <button type="submit">Search</button>
    </form>
    <div id="searchMessage" class="hidden">Here are the product details...</div> <!-- Hidden text -->
</div>

<div class="product-info">
    <h3>Features</h3>
    <div class="feature-container">
        <div class="feature">
            <img src="packaging_info.jpg" alt="Packaging Info">
            <h4>Packaging Info</h4>
            <p>Details about the packaging and reusability score.</p>
        </div>
        <div class="feature">
            <img src="reusability.jpg" alt="Reusability Score">
            <h4>Reusability Score</h4>
            <p>Rating indicating how easily the product can be reused or recycled.</p>
        </div>
        <div class="feature">
            <img src="health.jpeg" alt="Health Labels">
            <h4>Health Labels</h4>
            <p>Information about health labels and certifications.</p>
        </div>
        <div class="feature">
            <img src="allergens.png" alt="Allergens">
            <h4>Allergens</h4>
            <p>List of allergens present in the product.</p>
        </div>
    </div>
</div>
</div>
<footer style="background: url('background.jpeg') no-repeat center center/cover; color: #fff; padding: 30px 0; font-family: 'Roboto', sans-serif; text-align: center; position: relative;">
    <!-- Semi-transparent overlay to ensure text is readable -->
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.3);"></div>

    <div class="contact-info" style="font-size: 16px; color: #fff; margin-bottom: 20px; z-index: 1;">
        <p style="font-size: 20px; font-weight: 600; margin-bottom: 10px;">Need Assistance?</p>
        <p style="font-weight: 300; margin: 5px 0; font-size: 14px;">24/7 Support Available</p>
        <p style="font-weight: 500; margin: 5px 0; font-size: 16px;">Contact Us: (+374) 00-000-000</p>
        <p style="font-weight: 500; margin: 5px 0; font-size: 16px; text-decoration: underline; color: #007BFF;">support@recycleme.io</p>
    </div>
    <div class="social-icons" style="margin-top: 20px; z-index: 10; position: relative;">
        <a href="https://instagram.com" target="_blank" rel="noopener noreferrer">
            <img src="instagram.jpg" alt="Instagram" width="30" height="30" style="margin: 0 15px; transition: transform 0.3s ease;">
        </a>
        <a href="https://facebook.com" target="_blank" rel="noopener noreferrer">
            <img src="facebook1.jpg" alt="Facebook" width="30" height="30" style="margin: 0 15px; transition: transform 0.3s ease;">
        </a>
        <a href="https://twitter.com" target="_blank" rel="noopener noreferrer">
            <img src="twitter1.png" alt="Twitter" width="30" height="30" style="margin: 0 15px; transition: transform 0.3s ease;">
        </a>
    </div>
    <div class="copyright" style="font-size: 16px; margin-bottom: 20px; font-weight: 400; color: #fff; text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3); z-index: 1;">
        <p>© 2024 RecycleMe. All Rights Reserved.</p>
    </div>
</footer>
<script>
    const productFeatures = [
        { name: "Packaging Info", img: "packaging_info.jpg", description: "Details about the packaging and reusability score." },
        { name: "Reusability Score", img: "reusability.jpg", description: "Rating indicating how easily the product can be reused or recycled." },
        { name: "Health Labels", img: "health.jpeg", description: "Information about health labels and certifications." },
        { name: "Allergens", img: "allergens.png", description: "List of allergens present in the product." }
    ];

    // Function to dynamically populate the feature section
    function populateFeatures(features) {
        const featureContainer = document.querySelector('.feature-container');
        featureContainer.innerHTML = ''; // Clear any existing content

        features.forEach(feature => {
            const featureElement = document.createElement('div');
            featureElement.classList.add('feature');

            featureElement.innerHTML = `
            <img src="${feature.img}" alt="${feature.name}">
            <h4>${feature.name}</h4>
            <p>${feature.description}</p>
        `;

            featureContainer.appendChild(featureElement);
        });
    }

    // Call the function to populate features
    populateFeatures(productFeatures);

    function searchProduct(event) {
        event.preventDefault();
        // You can handle search functionality here
        document.querySelector('.product-info').style.display = 'block';
    }
</script>
<script>
    function searchProduct(event) {
        event.preventDefault();

        const message = document.getElementById('searchMessage');
        message.style.display = 'block'; // Show the message
        setTimeout(() => {
            message.style.opacity = '1'; // Fade in the message
        }, 100);
    }
</script>
<script>
    function fetchProductInfo(productName) {
        fetch(`/product_info/${productName}`)
            .then(response => response.json())
            .then(data => {
                // Display data on the page
                document.getElementById("product-name").innerText = data[0].name;
                document.getElementById("material").innerText = data[0].material;
                document.getElementById("recyclability").innerText = data[0].recyclability;
            })
            .catch(error => console.log('Error fetching product info:', error));
    }

    // Call function with a product name
    fetchProductInfo('Product A');
</script>
</body>
</html>

# Nearest Recycling point 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recycling Points</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #E5E5E5; /* Light gray background color */
            display: flex;
            flex-direction: column;
            align-items: center;
            transition: background-color 0.3s, color 0.3s;
        }

        header {
            background: url('background.jpeg') no-repeat center center/cover;
            color: #d3d3d3;
            height: 262.4px;
            width: 400px;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            font-family: 'Roboto', sans-serif;
            position: relative;
            box-sizing: border-box;
        }

        header h1 {
            position: relative;
            z-index: 1;
            font-size: 36px;
            margin: 0;
            font-weight: 600;
            color: #d3d3d3;
            text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
        }
        
        .recycling-info {
            margin-top: 20px;
            text-align: center;
            width: 80%;
        }

        .search-container {
            margin-bottom: 20px;
        }

        #map {
            width: 100%;
            height: 400px; /* Adjust the height as needed */
            margin-bottom: 20px;
        }

        #filters {
            background: linear-gradient(to right, #11400d, #0e3b07); /* Green gradient matching your theme */
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Optional subtle shadow for depth */
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between; /* Spread sections evenly */
            gap: 20px; /* Add space between sections */
            flex-wrap: wrap; /* Allow wrapping of sections in case of small screen size */
            padding: 20px;
            margin-bottom: 30px;
        }

        .filter-section {
            background-color: #f2f2f2; /* Light gray background */
            padding: 20px;
            border-radius: 10px; /* Rounded corners */
            text-align: center;
            width: 22%; /* Each section will take 22% of the width, adjust as needed */
            box-sizing: border-box;
            min-width: 250px; /* Minimum width to maintain readability */
        }

        .filter-section h3 {
            font-size: 18px;
            margin-bottom: 10px;
        }

        .filter-section label {
            margin-bottom: 10px;
            display: block;
        }

        .filter-section select, .filter-section input {
            width: 100%;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }

        .filter-section input[type="range"] {
            width: calc(100% - 40px); /* Adjust width of range input to fit */
        }

        #recycling-points {
            text-align: center;
            margin-top: 20px;
            width: 100%;
        }

        .recycling-card {
            background-color: #fff;
            padding: 20px;
            margin: 10px 0;
            border-radius: 8px;
            position: relative; /* To allow the gradient frame to be positioned */
        }

        .recycling-card::before {
            content: '';
            position: absolute;
            top: -8px;
            left: -8px;
            right: -8px;
            bottom: -8px;
            background: linear-gradient(to right, #11400d, #0e3b07); /* Green gradient matching your theme */
            border-radius: 10px;
            z-index: -1; /* Ensures the gradient stays behind the content */
        }

        .recycling-card h3, .recycling-card p {
            margin: 10px 0;
            font-size: 16px;
        }

        .recycling-card button {
            padding: 12px 20px;
            background-color: #11400d;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 15px;
            transition: background-color 0.3s;
            width: 100%;
            max-width: 200px;
        }

        .recycling-card button:hover {
            background-color: #0a2c06;
        }


        footer {
            background-color: #11400d;
            color: #fff; /* White text color */
            padding: 20px;
            margin-top: auto;
            text-align: center;
            width: 100%;
        }

        footer p {
            margin: 5px 0;
        }

        footer .social-icons {
            position: relative;
            z-index: 10;  /* Ensure it’s above the overlay */
        }
    </style>
</head>
<body>
<header>
    <h1>Find Recycling Points Near You</h1>
</header>

<div class="recycling-info">
    <div class="search-container">
        <input type="text" id="locationInput" placeholder="Enter location">
        <button onclick="searchRecyclingPoints()">Search</button>
        <button onclick="getLocation()">Use My Location</button>
    </div>
    <div id="map"></div>

    <div id="filters">
        <div class="filter-section">
            <h3>Filter by Distance</h3>
            <label for="distance">Distance (km):</label>
            <input type="range" id="distance" name="distance" min="1" max="100" step="1" value="10">
            <span id="distance-value">10 km</span>
        </div>

        <div class="filter-section">
            <h3>Filter by Day</h3>
            <label for="day">Select Day:</label>
            <input type="date" id="day" name="day">
        </div>

        <div class="filter-section">
            <h3>Select Materials</h3>
            <label for="materials">Select Materials:</label>
            <select id="materials" name="materials" onchange="filterRecyclingPoints()">
                <option value="all">All</option>
                <option value="plastic">Plastic</option>
                <option value="glass">Glass</option>
                <option value="paper">Paper</option>
                <option value="metal">Metal</option>
            </select>
        </div>

        <div class="filter-section">
            <h3>Select Services</h3>
            <label for="services">Select Services:</label>
            <select id="services" name="services">
                <option value="all">All</option>
                <option value="plastic-packaging-recycling" data-materials="plastic">Plastic Packaging Recycling</option>
                <option value="glass-items-recycling" data-materials="glass">Glass Items Recycling</option>
                <option value="compostable-packaging-recycling" data-materials="plastic, paper">Compostable Packaging Recycling</option>
                <option value="metal-can-recycling" data-materials="metal">Metal Can Recycling</option>
                <option value="tetra-pak-recycling" data-materials="paper">Tetra Pak Recycling</option>
            </select>
        </div>
    </div>

    <div id="recycling-points">
        <h2>Recycling Points in Yerevan</h2>

        <!-- Recycling Point 1 -->
        <div id="recycling-point-1" class="recycling-card">
            <h3>Center for Plastic Recycling</h3>
            <p><strong>Address:</strong> 1 Mamikonyants St, Yerevan</p>
            <p><strong>Contact:</strong> (374) 33-333-333</p>
            <p><strong>Accepted Materials:</strong> Plastic, Paper</p>
            <button onclick="centerMapOnLocation(40.207658, 44.526884)">View on Map</button> <!-- Mamikonyants 1 -->
        </div>

        <!-- Recycling Point 2 -->
        <div id="recycling-point-2" class="recycling-card">
            <h3>Eco Waste Recycling</h3>
            <p><strong>Address:</strong> 64 Komitas Ave, Yerevan</p>
            <p><strong>Contact:</strong> (374) 99-999-999</p>
            <p><strong>Accepted Materials:</strong> Glass, Metal</p>
            <button onclick="centerMapOnLocation(40.204742, 44.502191)">View on Map</button> <!-- 64 Komitas Avenue -->
        </div>
    </div>
</div>
<script>
    function updateRecyclingPoints() {
        const selectedMaterial = document.getElementById("materials").value;
        const selectedService = document.getElementById("services").value;

        // Get all recycling point elements
        const recyclingPoint1 = document.getElementById("recycling-point-1");
        const recyclingPoint2 = document.getElementById("recycling-point-2");

        // Show both points by default (when any filter is selected)
        recyclingPoint1.style.display = "block";
        recyclingPoint2.style.display = "block";

        // If specific material and service combination is selected, show only the corresponding recycling point
        if (
                (selectedMaterial === "plastic" && selectedService === "plastic-packaging-recycling") ||
                (selectedMaterial === "glass" && selectedService === "glass-items-recycling") ||
                (selectedMaterial === "compostable-packaging" && selectedService === "compostable-packaging-recycling")
        ) {
            recyclingPoint2.style.display = "none"; // Hide second point
        } else if (
                (selectedMaterial === "glass" && selectedService !== "glass-items-recycling") ||
                (selectedMaterial === "metal" && selectedService !== "metal-recycling")
        ) {
            recyclingPoint1.style.display = "none"; // Hide first point
        } else {
            // Default - show both recycling points when no specific filter combination is selected
            recyclingPoint1.style.display = "block";
            recyclingPoint2.style.display = "block";
        }
    }

    // Add event listeners for material and service changes
    window.onload = function() {
        document.getElementById("materials").addEventListener("change", updateRecyclingPoints);
        document.getElementById("services").addEventListener("change", updateRecyclingPoints);
        updateRecyclingPoints();  // Trigger initial check on page load
    };
</script>

<script>
    let map;
    // Function to initialize the map
    function initMap() {
        map = new google.maps.Map(document.getElementById("map"), {
            zoom: 12,
            center: {lat: 40.1811, lng: 44.5136} // Default to Yerevan
        });
    }

    // Function to center the map on the user's location
    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                const lat = position.coords.latitude;
                const lng = position.coords.longitude;
                console.log("User location:", lat, lng);  // Debugging: log coordinates

                // Center the map on the user's location
                map.setCenter(new google.maps.LatLng(lat, lng));

                // Remove the previous marker, if any
                if (userMarker) {
                    userMarker.setMap(null);
                }

                // Add a new marker at the user's location
                userMarker = new google.maps.Marker({
                    position: {lat, lng},
                    map: map,
                    title: "Your Location"
                });
            }, function(error) {
                console.log("Error occurred: ", error);  // Debugging: log any errors
                alert("Geolocation service failed.");
            });
        } else {
            alert("Your browser doesn't support geolocation.");
        }
    }
    // Function to center the map on a specific recycling center location
    function centerMapOnLocation(lat, lng) {
        const location = { lat, lng };
        map.setCenter(location); // Center the map on the selected location
        new google.maps.Marker({
            position: location,
            map: map,
            title: "Recycling Center"
        });
    }
</script>
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBlYmavsN8wBxs9045lu9uxSb_vIaiLzZQ&callback=initMap&libraries=places" async defer></script>
<footer style="background: url('background.jpeg') no-repeat center center/cover; color: #fff; padding: 30px 0; font-family: 'Roboto', sans-serif; text-align: center; position: relative;">
    <!-- Semi-transparent overlay to ensure text is readable -->
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.3);"></div>

    <div class="contact-info" style="font-size: 16px; color: #fff; margin-bottom: 20px; z-index: 1;">
        <p style="font-size: 20px; font-weight: 600; margin-bottom: 10px;">Need Assistance?</p>
        <p style="font-weight: 300; margin: 5px 0; font-size: 14px;">24/7 Support Available</p>
        <p style="font-weight: 500; margin: 5px 0; font-size: 16px;">Contact Us: (+374) 00-000-000</p>
        <p style="font-weight: 500; margin: 5px 0; font-size: 16px; text-decoration: underline; color: #007BFF;">support@recycleme.io</p>
    </div>
    <div class="social-icons" style="margin-top: 20px; z-index: 10; position: relative;">
        <a href="https://instagram.com" target="_blank" rel="noopener noreferrer">
            <img src="instagram.jpg" alt="Instagram" width="30" height="30" style="margin: 0 15px; transition: transform 0.3s ease;">
        </a>
        <a href="https://facebook.com" target="_blank" rel="noopener noreferrer">
            <img src="facebook1.jpg" alt="Facebook" width="30" height="30" style="margin: 0 15px; transition: transform 0.3s ease;">
        </a>
        <a href="https://twitter.com" target="_blank" rel="noopener noreferrer">
            <img src="twitter1.png" alt="Twitter" width="30" height="30" style="margin: 0 15px; transition: transform 0.3s ease;">
        </a>
    </div>
    <div class="copyright" style="font-size: 16px; margin-bottom: 20px; font-weight: 400; color: #fff; text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3); z-index: 1;">
        <p>© 2024 RecycleMe. All Rights Reserved.</p>
    </div>
</footer>
</body>
</html>


