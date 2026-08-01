const AI_SERVICE_URL = process.env.AI_SERVICE_URL || 'http://localhost:8000';

export async function fetchAiService(endpoint: string, payload: any) {
  const url = `${AI_SERVICE_URL}/api/v1/${endpoint}`;
  
  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error(`AI service error: ${response.statusText}`);
    }

    return await response.json();
  } catch (error) {
    console.error(`Failed to fetch AI service at ${url}:`, error);
    throw error;
  }
}
