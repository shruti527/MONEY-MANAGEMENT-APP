import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { prisma } from "@/lib/prisma";
import { Card } from "@/components/ui/Card";
import { ArrowUpRight, ArrowDownRight } from "lucide-react";
import { TransactionsChart } from "@/components/TransactionsChart";
import styles from "./page.module.css";

export default async function TransactionsPage() {
  const session = await getServerSession(authOptions);
  
  const transactions = await prisma.transaction.findMany({
    where: { userId: session?.user?.id },
    orderBy: { date: "desc" },
  });

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <h1 className="heading">All Transactions</h1>
        <p className={styles.subtitle}>Detailed view of your financial history</p>
      </header>

      <div className={styles.topSection}>
        <Card className={styles.chartCard} title="Expenditure Breakdown">
          <TransactionsChart transactions={transactions} />
        </Card>
      </div>

      <Card className={styles.tableCard}>
        {transactions.length > 0 ? (
          <div className={styles.tableWrapper}>
            <table className={styles.table}>
              <thead>
                <tr>
                  <th>Date</th>
                  <th>Category</th>
                  <th>Mode</th>
                  <th>Amount</th>
                </tr>
              </thead>
              <tbody>
                {transactions.map((t: any) => (
                  <tr key={t.id}>
                    <td>{new Date(t.date).toLocaleDateString()}</td>
                    <td>
                      <div className={styles.catWrapper}>
                        <div 
                          className={styles.tIcon} 
                          style={{ 
                            background: t.type === 'CREDIT' ? 'rgba(0, 187, 249, 0.1)' : 'rgba(255, 0, 84, 0.1)',
                            color: t.type === 'CREDIT' ? 'var(--success)' : 'var(--danger)'
                          }}
                        >
                          {t.type === 'CREDIT' ? <ArrowUpRight size={16} /> : <ArrowDownRight size={16} />}
                        </div>
                        {t.category || "Income"}
                      </div>
                    </td>
                    <td><span className={styles.badge}>{t.mode}</span></td>
                    <td className={t.type === 'CREDIT' ? styles.tCredit : styles.tDebit}>
                      {t.type === 'CREDIT' ? '+' : '-'}₹{t.amount.toLocaleString()}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <div className={styles.emptyState}>
            <p>No transactions found.</p>
          </div>
        )}
      </Card>
    </div>
  );
}
