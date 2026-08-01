"use client";

import { useState, useEffect } from "react";
import { Card } from "@/components/ui/Card";
import { Input } from "@/components/ui/Input";
import { Button } from "@/components/ui/Button";
import styles from "./page.module.css";

export default function ProfilePage() {
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
    occupation: "",
    mobileNumber: "",
  });
  
  const [loading, setLoading] = useState(false);
  const [initialLoading, setInitialLoading] = useState(true);
  const [message, setMessage] = useState({ type: "", text: "" });

  useEffect(() => {
    async function fetchProfile() {
      try {
        const res = await fetch("/api/profile");
        const data = await res.json();
        if (res.ok) {
          setFormData({
            firstName: data.firstName || "",
            lastName: data.lastName || "",
            email: data.email || "",
            occupation: data.occupation || "",
            mobileNumber: data.mobileNumber || "",
          });
        }
      } catch (err) {
        console.error("Failed to fetch profile", err);
      } finally {
        setInitialLoading(false);
      }
    }
    fetchProfile();
  }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setMessage({ type: "", text: "" });

    try {
      const res = await fetch("/api/profile", {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      if (!res.ok) {
        throw new Error("Failed to update profile");
      }

      setMessage({ type: "success", text: "Profile updated successfully!" });
    } catch (err: any) {
      setMessage({ type: "error", text: err.message });
    } finally {
      setLoading(false);
    }
  };

  if (initialLoading) {
    return <div style={{ padding: "40px", color: "rgba(255,255,255,0.5)" }}>Loading profile...</div>;
  }

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <h1 className="heading">Profile Settings</h1>
        <p className={styles.subtitle}>Update your personal details</p>
      </header>

      <div className={styles.formContainer}>
        <Card>
          {message.text && (
            <div className={message.type === 'success' ? styles.successAlert : styles.errorAlert}>
              {message.text}
            </div>
          )}

          <form onSubmit={handleSubmit} className={styles.form}>
            <div className={styles.grid2}>
              <Input 
                label="First Name" 
                name="firstName"
                value={formData.firstName}
                onChange={handleChange}
              />
              <Input 
                label="Last Name" 
                name="lastName"
                value={formData.lastName}
                onChange={handleChange}
              />
            </div>
            
            <Input 
              label="Email Address (Cannot be changed)" 
              name="email"
              type="email" 
              value={formData.email}
              disabled
            />

            <div className={styles.grid2}>
              <Input 
                label="Occupation" 
                name="occupation"
                placeholder="Software Engineer"
                value={formData.occupation}
                onChange={handleChange}
              />
              <Input 
                label="Mobile Number" 
                name="mobileNumber"
                placeholder="+1 234 567 890"
                value={formData.mobileNumber}
                onChange={handleChange}
              />
            </div>

            <div className={styles.actions}>
              <Button type="submit" disabled={loading}>
                {loading ? "Saving..." : "Update Profile"}
              </Button>
            </div>
          </form>
        </Card>
      </div>
    </div>
  );
}
