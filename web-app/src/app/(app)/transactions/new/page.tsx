"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Card } from "@/components/ui/Card";
import { Input } from "@/components/ui/Input";
import { Button } from "@/components/ui/Button";
import styles from "./page.module.css";

export default function AddTransactionPage() {
  const router = useRouter();
  const [type, setType] = useState<"CREDIT" | "DEBIT">("DEBIT");
  const [amount, setAmount] = useState("");
  const [date, setDate] = useState(new Date().toISOString().split('T')[0]);
  const [mode, setMode] = useState("Cash");
  const [category, setCategory] = useState("");
  
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      const res = await fetch("/api/transactions", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          type,
          amount: parseFloat(amount),
          date: new Date(date).toISOString(),
          mode,
          category,
        }),
      });

      if (!res.ok) {
        throw new Error("Failed to add transaction");
      }

      router.push("/dashboard");
      router.refresh();
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <h1 className="heading">New Transaction</h1>
        <p className={styles.subtitle}>Add a new credit or debit entry</p>
      </header>

      <div className={styles.formContainer}>
        <Card>
          {error && <div className={styles.errorAlert}>{error}</div>}
          
          <div className={styles.typeToggle}>
            <button 
              className={`${styles.toggleBtn} ${type === 'CREDIT' ? styles.activeCredit : ''}`}
              onClick={() => setType('CREDIT')}
            >
              Income
            </button>
            <button 
              className={`${styles.toggleBtn} ${type === 'DEBIT' ? styles.activeDebit : ''}`}
              onClick={() => setType('DEBIT')}
            >
              Expense
            </button>
          </div>

          <form onSubmit={handleSubmit} className={styles.form}>
            <div className={styles.grid2}>
              <Input 
                label="Amount (₹)" 
                type="number" 
                step="0.01"
                min="0"
                placeholder="0.00"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                required
              />
              <Input 
                label="Date" 
                type="date"
                value={date}
                onChange={(e) => setDate(e.target.value)}
                required
              />
            </div>

            <div className={styles.inputGroup}>
              <label className={styles.label}>Mode of Payment</label>
              <select 
                className={styles.select}
                value={mode}
                onChange={(e) => setMode(e.target.value)}
                required
              >
                <option value="Cash">Cash</option>
                <option value="Credit Card">Credit Card</option>
                <option value="Debit Card">Debit Card</option>
                <option value="UPI">UPI</option>
                <option value="Bank Transfer">Bank Transfer</option>
              </select>
            </div>

            <Input 
              label={type === 'CREDIT' ? 'Source of Income' : 'Money Spent On (Category)'} 
              type="text" 
              placeholder={type === 'CREDIT' ? 'e.g. Salary, Freelance' : 'e.g. Groceries, Rent'}
              value={category}
              onChange={(e) => setCategory(e.target.value)}
              required
            />

            <Button type="submit" fullWidth disabled={loading}>
              {loading ? "Saving..." : `Add ${type === 'CREDIT' ? 'Income' : 'Expense'}`}
            </Button>
          </form>
        </Card>
      </div>
    </div>
  );
}
