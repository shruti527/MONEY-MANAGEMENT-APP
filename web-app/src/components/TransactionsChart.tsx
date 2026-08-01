"use client";

import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip, Legend } from "recharts";
interface TransactionProp {
  type: string;
  amount: number;
  category: string | null;
}

const COLORS = ["#8a2be2", "#00f5d4", "#ff0054", "#00bbf9", "#fca311", "#4cc9f0"];

export function TransactionsChart({ transactions }: { transactions: TransactionProp[] }) {
  const debitTransactions = transactions.filter(t => t.type === "DEBIT");
  
  if (debitTransactions.length === 0) {
    return <div style={{ padding: "40px", textAlign: "center", color: "rgba(255,255,255,0.5)" }}>No expenses to visualize yet.</div>;
  }

  // Aggregate by category
  const dataMap = debitTransactions.reduce((acc: Record<string, number>, t) => {
    const cat = t.category || "Other";
    acc[cat] = (acc[cat] || 0) + t.amount;
    return acc;
  }, {});

  const data = Object.keys(dataMap).map((key) => ({
    name: key,
    value: dataMap[key],
  }));

  return (
    <div style={{ width: "100%", height: 300 }}>
      <ResponsiveContainer>
        <PieChart>
          <Pie
            data={data}
            cx="50%"
            cy="50%"
            innerRadius={60}
            outerRadius={100}
            paddingAngle={5}
            dataKey="value"
            stroke="none"
          >
            {data.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip 
            formatter={(value: any) => `₹${value.toLocaleString()}`}
            contentStyle={{ 
              background: "rgba(20, 20, 20, 0.9)", 
              border: "1px solid rgba(255,255,255,0.1)",
              borderRadius: "8px",
              color: "white"
            }}
          />
          <Legend />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}
