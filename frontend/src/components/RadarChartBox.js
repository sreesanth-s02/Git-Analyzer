import React from "react";
import {
  Radar, RadarChart, PolarGrid,
  PolarAngleAxis, PolarRadiusAxis
} from "recharts";

const RadarChartBox = ({ data }) => {
  const chartData = [
    { subject: "Quality", A: data.quality_score },
    { subject: "Relevance", A: data.relevance_score },
    { subject: "Depth", A: data.depth_score },
    { subject: "Consistency", A: data.consistency_score },
    { subject: "Auth", A: data.authenticity_score },
  ];

  return (
    <RadarChart outerRadius={90} width={400} height={300} data={chartData}>
      <PolarGrid />
      <PolarAngleAxis dataKey="subject" />
      <PolarRadiusAxis />
      <Radar dataKey="A" stroke="#4ade80" fill="#4ade80" fillOpacity={0.6} />
    </RadarChart>
  );
};

export default RadarChartBox;