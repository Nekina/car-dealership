import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import "./Dealers.css";
import "../assets/style.css";
import positive_icon from "../assets/positive.png";
import neutral_icon from "../assets/neutral.png";
import negative_icon from "../assets/negative.png";
import review_icon from "../assets/reviewbutton.png";
import Header from "../Header/Header";

const Dealer = () => {
  const [dealer, setDealer] = useState(null);
  const [reviews, setReviews] = useState([]);
  const [unreviewed, setUnreviewed] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [postReview, setPostReview] = useState(null);

  // Build URLs
  const curr_url = window.location.href;
  const root_url = curr_url.substring(0, curr_url.indexOf("dealer"));
  const params = useParams();
  const id = params.id;
  const dealer_url = root_url + `djangoapp/dealer/${id}`;
  const reviews_url = root_url + `djangoapp/reviews/dealer/${id}`;
  const post_review = root_url + `postreview/${id}`;

  // Fetch dealer data
  const get_dealer = async () => {
    try {
      const res = await fetch(dealer_url);
      const retobj = await res.json();

      if (retobj.status === 200) {
        console.log("Dealer fetch success:", retobj.dealer);

        // Ensure we set the first object from the array
        if (Array.isArray(retobj.dealer) && retobj.dealer.length > 0) {
          setDealer(retobj.dealer[0]);
        } else {
          setError("No dealer data found.");
        }
      } else {
        setError("Failed to fetch dealer details.");
      }
    } catch (err) {
      console.error("Dealer fetch error:", err);
      setError("Failed to fetch dealer details.");
    }
  };

  // Fetch reviews data
  const get_reviews = async () => {
    try {
      const res = await fetch(reviews_url);
      const retobj = await res.json();

      if (retobj.status === 200) {
        console.log("Reviews fetch success:", retobj.reviews);

        if (Array.isArray(retobj.reviews) && retobj.reviews.length > 0) {
          setReviews(retobj.reviews);
        } else {
          setUnreviewed(true);
        }
      } else {
        setError("Failed to fetch reviews.");
      }
    } catch (err) {
      console.error("Reviews fetch error:", err);
      setError("Failed to fetch reviews.");
    }
  };

  // Choose sentiment icon
  const senti_icon = (sentiment) => {
    return sentiment === "positive"
      ? positive_icon
      : sentiment === "negative"
      ? negative_icon
      : neutral_icon;
  };

  // Load data on mount
  useEffect(() => {
    const fetchData = async () => {
      await get_dealer();
      await get_reviews();
      setLoading(false);
    };

    fetchData();

    // Setup post review button if user logged in
    if (sessionStorage.getItem("username")) {
      setPostReview(
        <a href={post_review}>
          <img
            src={review_icon}
            style={{ width: "10%", marginLeft: "10px", marginTop: "10px" }}
            alt="Post Review"
          />
        </a>
      );
    }
  }, []);

  return (
    <div style={{ margin: "20px" }}>
      <Header />

      {loading ? (
        <p>Loading dealer details...</p>
      ) : error ? (
        <p style={{ color: "red" }}>{error}</p>
      ) : (
        <>
          <div style={{ marginTop: "10px" }}>
            <h1 style={{ color: "grey" }}>
              {dealer?.full_name || dealer?.name} {postReview}
            </h1>
            <h4 style={{ color: "grey" }}>
              {dealer?.city}, {dealer?.address}, Zip - {dealer?.zip},{" "}
              {dealer?.state}
            </h4>
          </div>

          <div className="reviews_panel">
            {reviews.length === 0 && !unreviewed ? (
              <p>Loading Reviews...</p>
            ) : unreviewed ? (
              <div>No reviews yet!</div>
            ) : (
              reviews.map((review, index) => (
                <div key={index} className="review_panel">
                  <img
                    src={senti_icon(review.sentiment)}
                    className="emotion_icon"
                    alt="Sentiment"
                  />
                  <div className="review">{review.review}</div>
                  <div className="reviewer">
                    {review.name} {review.car_make} {review.car_model}{" "}
                    {review.car_year}
                  </div>
                </div>
              ))
            )}
          </div>
        </>
      )}
    </div>
  );
};

export default Dealer;
