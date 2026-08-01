'use server';

import { prisma } from '@/lib/prisma';
import { getServerSession } from 'next-auth';
import { authOptions } from '@/lib/auth';
import { fetchAiService } from '@/lib/ai-client';

async function getUserTransactions() {
  const session = await getServerSession(authOptions);
  
  if (!session?.user?.email) {
    throw new Error('Unauthorized');
  }

  const user = await prisma.user.findUnique({
    where: { email: session.user.email },
  });

  if (!user) {
    throw new Error('User not found');
  }

  const transactions = await prisma.transaction.findMany({
    where: { userId: user.id },
    orderBy: { date: 'asc' },
  });

  return transactions.map(t => ({
    id: t.id,
    category: t.category,
    amount: t.amount,
    date: t.date.toISOString().split('T')[0], // format as YYYY-MM-DD
  }));
}

export async function getPredictSpending() {
  const transactions = await getUserTransactions();
  return fetchAiService('predict-spending', { transactions });
}

export async function getDetectAnomalies() {
  const transactions = await getUserTransactions();
  return fetchAiService('detect-anomalies', { transactions });
}

export async function getBudgetInsights(monthlyIncome: number = 5000) {
  const transactions = await getUserTransactions();
  return fetchAiService('budget-insights', { 
    transactions, 
    monthly_income: monthlyIncome 
  });
}
