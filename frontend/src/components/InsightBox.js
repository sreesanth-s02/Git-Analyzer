import React from "react";

const InsightBox = ({ data }) => {
  return (
    <div className="insight-ai">
      <h3>AI Insight</h3>

      <p>
        Based on your GitHub profile, you show strong consistency and
        authentic project work. However, your alignment with the selected
        role could be improved by focusing on key technologies.
      </p>

      <p className="recommend">
        👉 Focus on improving missing skills to boost your score.
      </p>
    </div>
  );
};

export default InsightBox;