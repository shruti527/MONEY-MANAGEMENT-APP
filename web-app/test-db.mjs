import { createClient } from '@libsql/client';
import dotenv from 'dotenv';
dotenv.config();

async function main() {
  const url = process.env.TURSO_DATABASE_URL;
  const authToken = process.env.TURSO_AUTH_TOKEN;

  if (!url) {
    console.error("TURSO_DATABASE_URL is missing in .env");
    process.exit(1);
  }

  console.log("Connecting to:", url);
  const client = createClient({ url, authToken });

  try {
    console.log("Creating User table...");
    await client.execute(`CREATE TABLE IF NOT EXISTS "User" (
        "id" TEXT NOT NULL PRIMARY KEY,
        "email" TEXT NOT NULL,
        "password" TEXT NOT NULL,
        "firstName" TEXT,
        "lastName" TEXT,
        "occupation" TEXT,
        "mobileNumber" TEXT,
        "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        "updatedAt" DATETIME NOT NULL
    );`);

    console.log("Creating Transaction table...");
    await client.execute(`CREATE TABLE IF NOT EXISTS "Transaction" (
        "id" TEXT NOT NULL PRIMARY KEY,
        "amount" REAL NOT NULL,
        "date" DATETIME NOT NULL,
        "type" TEXT NOT NULL,
        "mode" TEXT NOT NULL,
        "category" TEXT,
        "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        "updatedAt" DATETIME NOT NULL,
        "userId" TEXT NOT NULL,
        CONSTRAINT "Transaction_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User" ("id") ON DELETE CASCADE ON UPDATE CASCADE
    );`);

    console.log("Creating Index...");
    await client.execute(`CREATE UNIQUE INDEX IF NOT EXISTS "User_email_key" ON "User"("email");`);

    console.log("Success! Tables created in Turso.");
  } catch (err) {
    console.error("Database connection failed:", err);
  }
}
main();
