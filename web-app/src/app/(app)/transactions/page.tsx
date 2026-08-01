import Link from "next/link";
import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { prisma } from "@/lib/prisma";
import { Card } from "@/components/ui/Card";
import { ArrowUpRight, ArrowDownRight } from "lucide-react";
import { TransactionsChart } from "@/components/TransactionsChart";
import styles from "./page.module.css";

export default async function TransactionsPage({ searchParams }: { searchParams?: { page?: string } }) {
  const session = await getServerSession(authOptions);
  const pageSize = 10;
  const requestedPage = parseInt(searchParams?.page ?? "1", 10);
  const currentPage = Number.isNaN(requestedPage) || requestedPage < 1 ? 1 : requestedPage;

  const totalCount = await prisma.transaction.count({
    where: { userId: session?.user?.id },
  });

  const totalPages = Math.max(1, Math.ceil(totalCount / pageSize));
  const page = Math.min(currentPage, totalPages);
  const offset = (page - 1) * pageSize;

  const transactions = await prisma.transaction.findMany({
    where: { userId: session?.user?.id },
    orderBy: { date: "desc" },
    skip: offset,
    take: pageSize,
  });

  const startItem = totalCount === 0 ? 0 : offset + 1;
  const endItem = offset + transactions.length;

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

      <div className={styles.pagination}>
        <span className={styles.pageInfo}>
          Showing {startItem}–{endItem} of {totalCount} transactions
        </span>
        <div className={styles.paginationButtons}>
          <Link
            href={`/transactions?page=${page - 1}`}
            className={`${styles.pageButton} ${page <= 1 ? styles.pageButtonDisabled : ''}`}
          >
            Previous
          </Link>
          <Link
            href={`/transactions?page=${page + 1}`}
            className={`${styles.pageButton} ${page >= totalPages ? styles.pageButtonDisabled : ''}`}
          >
            Next
          </Link>
        </div>
      </div>
    </div>
  );
}