import React, { useState, useEffect } from "react";
import axios from "axios";
import Chart from "react-apexcharts";

export default function Dashboard() {
  const [msg, setmsg] = useState({
    options: {
      chart: {
        id: "basic-bar"
      },
      xaxis: {
        categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]
      }
    },
    series: [
      {
        name: "series-1",
        data: [30, 40, 45, 50, 49, 60, 70, 91]
      }
    ]
  });

  useEffect(() => {
    axios
      .get("/esp2")
      .then((resp) => setmsg(resp.data))
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <Chart
              options={msg.options}
              series={msg.series}
              type="bar"
              width="1000"
            />
      {/* {Object.keys(msg).map((key) => (
        <p>
          {key} : {msg[key]}
        </p>
      ))}{" "} */}
    </div>
  );
}
