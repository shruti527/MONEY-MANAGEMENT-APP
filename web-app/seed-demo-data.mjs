import { PrismaClient } from '@prisma/client';
import { PrismaLibSql } from '@prisma/adapter-libsql';
import bcrypt from 'bcryptjs';
import dotenv from 'dotenv';
dotenv.config();

const EMAIL = 'shrutichedge@gmail.com';
const PASSWORD = '123456';

const adapter = new PrismaLibSql({
  url: process.env.TURSO_DATABASE_URL,
  authToken: process.env.TURSO_AUTH_TOKEN,
});
const prisma = new PrismaClient({ adapter });

const months = [
  { year: 2025, month: 12 },
  { year: 2026, month: 1 },
  { year: 2026, month: 2 },
  { year: 2026, month: 3 },
  { year: 2026, month: 4 },
  { year: 2026, month: 5 },
  { year: 2026, month: 6 },
  { year: 2026, month: 7 },
];

function iso(y, m, d) {
  return new Date(Date.UTC(y, m - 1, d, 9, 0, 0)).toISOString();
}

function buildTransactions(userId) {
  const rows = [];

  months.forEach(({ year, month }, m) => {
    rows.push({ type: 'CREDIT', amount: 85000, date: iso(year, month, 1), mode: 'Bank Transfer', category: 'Salary', userId });
    rows.push({ type: 'DEBIT', amount: 24000, date: iso(year, month, 3), mode: 'Bank Transfer', category: 'Housing', userId });
    rows.push({ type: 'DEBIT', amount: 5500 + m * 250, date: iso(year, month, 5), mode: 'UPI', category: 'Groceries', userId });
    rows.push({ type: 'DEBIT', amount: 1800 + m * 120, date: iso(year, month, 8), mode: 'UPI', category: 'Utilities', userId });
    rows.push({ type: 'DEBIT', amount: 1100 + m * 80, date: iso(year, month, 9), mode: 'UPI', category: 'Utilities', userId });
    rows.push({ type: 'DEBIT', amount: 1600 + m * 150, date: iso(year, month, 10), mode: 'Credit Card', category: 'Transportation', userId });
    rows.push({ type: 'DEBIT', amount: 900 + m * 90, date: iso(year, month, 12), mode: 'UPI', category: 'Healthcare', userId });
    rows.push({ type: 'DEBIT', amount: 2300 + m * 220, date: iso(year, month, 14), mode: 'Credit Card', category: 'Dining', userId });
    rows.push({ type: 'DEBIT', amount: 950 + m * 140, date: iso(year, month, 18), mode: 'UPI', category: 'Entertainment', userId });
    rows.push({ type: 'DEBIT', amount: 3400 + m * 450, date: iso(year, month, 21), mode: 'Credit Card', category: 'Shopping', userId });
    rows.push({ type: 'DEBIT', amount: 1700 + m * 150, date: iso(year, month, 25), mode: 'Cash', category: 'Dining', userId });
  });

  rows.push({ type: 'DEBIT', amount: 12500, date: iso(2025, 12, 20), mode: 'Credit Card', category: 'Travel', userId });
  rows.push({ type: 'DEBIT', amount: 16500, date: iso(2026, 4, 16), mode: 'Credit Card', category: 'Travel', userId });
  rows.push({ type: 'DEBIT', amount: 23500, date: iso(2026, 7, 22), mode: 'Credit Card', category: 'Travel', userId });

  rows.push({ type: 'DEBIT', amount: 64000, date: iso(2026, 5, 20), mode: 'Credit Card', category: 'Shopping', userId });
  rows.push({ type: 'DEBIT', amount: 27500, date: iso(2026, 6, 17), mode: 'UPI', category: 'Healthcare', userId });

  return rows;
}

const hashed = bcrypt.hashSync(PASSWORD, 10);

const user = await prisma.user.upsert({
  where: { email: EMAIL },
  update: { firstName: 'Shruti', lastName: 'Chedge', password: hashed },
  create: { email: EMAIL, firstName: 'Shruti', lastName: 'Chedge', password: hashed },
});

await prisma.transaction.deleteMany({ where: { userId: user.id } });

const rows = buildTransactions(user.id);
await prisma.transaction.createMany({ data: rows });

const count = await prisma.transaction.count({ where: { userId: user.id } });
const credit = await prisma.transaction.aggregate({ where: { userId: user.id, type: 'CREDIT' }, _sum: { amount: true } });
const debit = await prisma.transaction.aggregate({ where: { userId: user.id, type: 'DEBIT' }, _sum: { amount: true } });

console.log(`User: ${user.firstName} ${user.lastName} <${user.email}> (password: ${PASSWORD})`);
console.log(`Inserted ${count} transactions`);
console.log(`Total CREDIT: ${credit._sum.amount}`);
console.log(`Total DEBIT: ${debit._sum.amount}`);

await prisma.$disconnect();
