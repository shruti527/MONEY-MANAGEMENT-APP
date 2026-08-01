import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { prisma } from "@/lib/prisma";
import { Card } from "@/components/ui/Card";
import { ArrowUpRight, ArrowDownRight, IndianRupee, BrainCircuit, AlertTriangle, TrendingUp } from "lucide-react";
import styles from "./page.module.css";
import { getPredictSpending, getDetectAnomalies, getBudgetInsights } from "@/app/actions/ai";

export default async function DashboardPage() {
  const session = await getServerSession(authOptions);
  
  const transactions = await prisma.transaction.findMany({
    where: { userId: session?.user?.id },
    orderBy: { date: "desc" },
    take: 5,
  });

  const allTransactions = await prisma.transaction.findMany({
    where: { userId: session?.user?.id },
  });

  const totalCredit = allTransactions
    .filter((t: any) => t.type === "CREDIT")
    .reduce((sum: number, t: any) => sum + t.amount, 0);

  const totalDebit = allTransactions
    .filter((t: any) => t.type === "DEBIT")
    .reduce((sum: number, t: any) => sum + t.amount, 0);

  const balance = totalCredit - totalDebit;

  let aiInsights = null;
  let anomalies = null;
  let predictions = null;

  try {
    const monthlyIncome = totalCredit > 0 ? totalCredit : 5000;
    const [insightsRes, anomaliesRes, predictRes] = await Promise.all([
      getBudgetInsights(monthlyIncome),
      getDetectAnomalies(),
      getPredictSpending()
    ]);
    aiInsights = insightsRes;
    anomalies = anomaliesRes?.anomalies || [];
    predictions = predictRes?.predictions || [];
  } catch (err) {
    console.error("AI Service Error:", err);
  }

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <div>
          <h1 className="heading">Dashboard</h1>
          <p className={styles.subtitle}>Welcome back, {session?.user?.name || "User"}!</p>
        </div>
      </header>

      <div className={styles.statsGrid}>
        <Card className={styles.statCard}>
          <div className={styles.statIconWrapper} style={{ background: "rgba(138, 43, 226, 0.2)", color: "var(--primary)" }}>
            <IndianRupee size={24} />
          </div>
          <div>
            <p className={styles.statLabel}>Total Balance</p>
            <h2 className={styles.statValue}>₹{balance.toLocaleString()}</h2>
          </div>
        </Card>
        
        <Card className={styles.statCard}>
          <div className={styles.statIconWrapper} style={{ background: "rgba(0, 187, 249, 0.2)", color: "var(--success)" }}>
            <ArrowUpRight size={24} />
          </div>
          <div>
            <p className={styles.statLabel}>Total Income</p>
            <h2 className={styles.statValue}>₹{totalCredit.toLocaleString()}</h2>
          </div>
        </Card>

        <Card className={styles.statCard}>
          <div className={styles.statIconWrapper} style={{ background: "rgba(255, 0, 84, 0.2)", color: "var(--danger)" }}>
            <ArrowDownRight size={24} />
          </div>
          <div>
            <p className={styles.statLabel}>Total Expenses</p>
            <h2 className={styles.statValue}>₹{totalDebit.toLocaleString()}</h2>
          </div>
        </Card>
      </div>

      <div className={styles.aiSection}>
        <h2 className="heading">AI Insights & Predictions</h2>
        <div className={styles.aiGrid}>
          
          <div className={styles.aiCard}>
            <div className={styles.aiCardHeader}>
              <div className={styles.statIconWrapper} style={{ background: "rgba(0, 187, 249, 0.2)", color: "var(--success)" }}>
                <BrainCircuit size={24} />
              </div>
              <h3 className={styles.aiTitle}>Budget Analysis</h3>
            </div>
            <p className={styles.aiDesc}>
              {aiInsights?.message || "Not enough data for budget insights yet. Add more transactions."}
            </p>
          </div>

          <div className={styles.aiCard}>
            <div className={styles.aiCardHeader}>
              <div className={styles.statIconWrapper} style={{ background: "rgba(255, 0, 84, 0.2)", color: "var(--danger)" }}>
                <AlertTriangle size={24} />
              </div>
              <h3 className={styles.aiTitle}>Anomalies</h3>
            </div>
            <p className={styles.aiDesc}>
              {anomalies && anomalies.length > 0 
                ? `Detected ${anomalies.length} unusual transactions recently.` 
                : "No unusual spending patterns detected. Keep it up!"}
            </p>
          </div>

          <div className={styles.aiCard}>
            <div className={styles.aiCardHeader}>
              <div className={styles.statIconWrapper} style={{ background: "rgba(138, 43, 226, 0.2)", color: "var(--primary)" }}>
                <TrendingUp size={24} />
              </div>
              <h3 className={styles.aiTitle}>Predicted Spending</h3>
            </div>
            <p className={styles.aiDesc}>
              {predictions && predictions.length > 0 
                ? `Highest expected spend: ${predictions[0].category} (₹${predictions[0].projected_amount.toFixed(0)})`
                : "Need more data to predict your future spending."}
            </p>
          </div>

        </div>
      </div>

      <div className={styles.recentSection}>
        <h2 className="heading">Recent Transactions</h2>
        <Card className={styles.tableCard}>
          {transactions.length > 0 ? (
            <div className={styles.transactionList}>
              {transactions.map((t: any) => (
                <div key={t.id} className={styles.transactionItem}>
                  <div className={styles.tLeft}>
                    <div 
                      className={styles.tIcon} 
                      style={{ 
                        background: t.type === 'CREDIT' ? 'rgba(0, 187, 249, 0.1)' : 'rgba(255, 0, 84, 0.1)',
                        color: t.type === 'CREDIT' ? 'var(--success)' : 'var(--danger)'
                      }}
                    >
                      {t.type === 'CREDIT' ? <ArrowUpRight size={20} /> : <ArrowDownRight size={20} />}
                    </div>
                    <div>
                      <p className={styles.tTitle}>{t.category || "Income"}</p>
                      <p className={styles.tDate}>{new Date(t.date).toLocaleDateString()}</p>
                    </div>
                  </div>
                  <div className={styles.tRight}>
                    <span className={t.type === 'CREDIT' ? styles.tCredit : styles.tDebit}>
                      {t.type === 'CREDIT' ? '+' : '-'}₹{t.amount.toLocaleString()}
                    </span>
                    <p className={styles.tMode}>{t.mode}</p>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className={styles.emptyState}>
              <p>No transactions found. Start by adding one!</p>
            </div>
          )}
        </Card>
      </div>
    </div>
  );
}
