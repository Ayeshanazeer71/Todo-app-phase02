const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api";

async function request(endpoint: string, options: any = {}) {
  const token = typeof window !== 'undefined' ? localStorage.getItem("auth_token") : null;
  const headers: any = {
    ...options.headers,
  };

  if (!(options.body instanceof FormData)) {
    headers["Content-Type"] = "application/json";
  }

  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  const response = await fetch(`${API_URL}${endpoint}`, {
    ...options,
    headers,
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || "Something went wrong");
  }

  return response.json();
}

export const api = {
  // Auth
  login: async (formData: FormData) => {
    const res = await request("/auth/login", {
      method: "POST",
      body: formData,
    });
    localStorage.setItem("auth_token", res.access_token);
    return res;
  },
  signup: async (data: any) => {
    const res = await request("/auth/signup", {
      method: "POST",
      body: JSON.stringify(data),
    });
    localStorage.setItem("auth_token", res.access_token);
    return res;
  },
  logout: () => {
    localStorage.removeItem("auth_token");
    window.location.href = "/login";
  },

  // Tasks
  getTasks: () => request("/tasks/"),
  createTask: (data: { title: string; description?: string; deadline?: string; priority?: string; category?: string; subtasks?: any[]; position?: number }) =>
    request("/tasks/", { method: "POST", body: JSON.stringify(data) }),
  updateTask: (id: number, data: any) =>
    request(`/tasks/${id}`, { method: "PUT", body: JSON.stringify(data) }),
  deleteTask: (id: number) =>
    request(`/tasks/${id}`, { method: "DELETE" }),
  toggleComplete: (id: number) =>
    request(`/tasks/${id}/complete`, { method: "PATCH" }),
};
