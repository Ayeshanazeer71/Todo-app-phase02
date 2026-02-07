"use client";

import { useState } from "react";
import { api } from "@/lib/api";
import { useRouter } from "next/navigation";
import Link from "next/link";

type Mode = "login" | "signup";

export default function AuthPage() {
  const [mode, setMode] = useState<Mode>("login");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const router = useRouter();

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError("");

    if (mode === "login") {
      const formData = new FormData();
      formData.append("username", username);
      formData.append("password", password);
      try {
        await api.login(formData);
        router.push("/");
      } catch (err: any) {
        setError(err.message || "Invalid credentials");
      }
    } else {
      try {
        await api.signup({ username, password });
        router.push("/");
      } catch (err: any) {
        setError(err.message || "Failed to create account");
      }
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-600 via-blue-700 to-indigo-800 p-4">
      <div className="w-full max-w-md">
        <div className="bg-white rounded-2xl shadow-xl border border-gray-100 p-8">
          <div className="flex rounded-xl bg-gray-100 p-1 mb-6">
            <button
              type="button"
              onClick={() => { setMode("login"); setError(""); }}
              className={`flex-1 py-2.5 rounded-lg text-sm font-bold transition-all ${mode === "login" ? "bg-white text-blue-600 shadow" : "text-gray-500 hover:text-gray-700"}`}
            >
              Log in
            </button>
            <button
              type="button"
              onClick={() => { setMode("signup"); setError(""); }}
              className={`flex-1 py-2.5 rounded-lg text-sm font-bold transition-all ${mode === "signup" ? "bg-white text-blue-600 shadow" : "text-gray-500 hover:text-gray-700"}`}
            >
              Sign up
            </button>
          </div>

          <h2 className="text-xl font-bold text-gray-800 mb-6 text-center">
            {mode === "login" ? "Welcome back" : "Create your account"}
          </h2>

          {error && (
            <p className="mb-4 p-3 rounded-xl bg-red-50 text-red-600 text-sm text-center border border-red-100">
              {error}
            </p>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block mb-1.5 text-sm font-medium text-gray-600">Username</label>
              <input
                type="text"
                className="w-full px-4 py-3 border border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>
            <div>
              <label className="block mb-1.5 text-sm font-medium text-gray-600">Password</label>
              <input
                type="password"
                className="w-full px-4 py-3 border border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
            <button
              type="submit"
              className={`w-full py-3.5 rounded-xl font-bold text-white shadow-md hover:opacity-95 active:scale-[0.98] transition-all ${mode === "login" ? "bg-blue-600 hover:bg-blue-700" : "bg-green-600 hover:bg-green-700"}`}
            >
              {mode === "login" ? "Sign in" : "Create account"}
            </button>
          </form>
        </div>
        <p className="mt-6 text-center text-sm text-white/90">
          Phase II Todo — sign in or create an account to continue.
        </p>
      </div>
    </div>
  );
}
