import React from 'react';
import { Sidebar } from './Sidebar';
import styles from './AppLayout.module.css';

export function AppLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className={styles.layout}>
      <Sidebar />
      <main className={styles.main}>
        <div className={styles.contentWrapper}>
          {children}
        </div>
      </main>
    </div>
  );
}
