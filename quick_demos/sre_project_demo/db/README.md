### **Access the Database Using `keinos/sqlite3`**

1. **Start the Containers**:
   ```bash
   docker-compose up --build
   ```

2. **Access the `db` Container**:
   Use the following command to open a shell inside the `db` container:
   ```bash
   docker exec -it <db_container_name> sh
   ```

   Replace `<db_container_name>` with the actual name of the `db` container. You can find it using `docker ps`.

3. **Open the SQLite CLI**:
   Inside the container, use the SQLite CLI to open the database:
   ```bash
   sqlite3 analytics.db
   ```

4. **Run Queries**:
   Use standard SQLite commands to interact with the database:
   - Show all tables:
     ```sql
     .tables
     ```
   - View the structure of the `analytics` table:
     ```sql
     PRAGMA table_info(analytics);
     ```
   - View all data in the `analytics` table:
     ```sql
     SELECT * FROM analytics;
     ```

5. **Exit SQLite**:
   To exit the SQLite CLI, type:
   ```bash
   .exit
   ```

---

### Additional Notes:
- **Container Interdependence**: The Flask app and the SQLite container work together by sharing the `./db` directory. Any updates to the database file by one container will be immediately available to the other.
- **SQLite GUI Tools**: If you want a GUI tool for SQLite, you can still open the `./db/analytics.db` file from your host machine while the containers are running.

Let me know if you need further clarification!