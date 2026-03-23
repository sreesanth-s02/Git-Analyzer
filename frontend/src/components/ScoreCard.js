import React from "react";
import { motion } from "framer-motion";

const ScoreCard = ({ score, category }) => {
  return (
    <motion.div
      className="score-card"
      initial={{ scale: 0.8, opacity: 0 }}
      animate={{ scale: 1, opacity: 1 }}
    >
      <h2>{score}</h2>

      <div className="circle">
        <div
          className="circle-fill"
          style={{ transform: `rotate(${score * 1.8}deg)` }}
        ></div>
      </div>

      <p className={`badge ${category}`}>{category}</p>
    </motion.div>
  );
};

export default ScoreCard;